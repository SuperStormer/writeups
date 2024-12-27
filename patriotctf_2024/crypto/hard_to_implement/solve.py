import itertools
import string

from pwn import *
from utils.crypto.aes.attacks import detect_blocksize
from utils.itertools2 import grouper
from utils.num.misc import round_to_multiple

p = remote("chal.competitivecyber.club", 6001)


def decrypt_ecb_suffix(oracle):
	# see cryptopals #12/#14
	block_size: int = detect_blocksize(oracle)

	# get prefix length
	common_prefix = None
	prefix_len = None
	for i in range(block_size):
		padding = b"A" * (i + 2 * block_size)
		blocks = list(grouper(oracle(padding), block_size))
		for j, b1, b2 in zip(itertools.count(), blocks, blocks[1:]):
			if b1 == b2:
				common_prefix = padding
				prefix_len = (j + 2) * block_size
				break
		else:
			continue
		break
	if common_prefix is None:
		raise ValueError("Couldn't find prefix length")
	assert prefix_len is not None
	length = round_to_multiple(len(oracle(common_prefix)) - prefix_len, block_size)
	known = bytearray()
	for j in range(length):
		prefix = common_prefix + b"A" * (length - j - 1)
		encrypted = oracle(prefix)[: length + prefix_len]

		for c in (
			string.ascii_lowercase
			+ "{}"
			+ string.digits
			+ string.ascii_uppercase
			+ string.punctuation
		).encode():
			encrypted2 = oracle(prefix + known + bytes((c,)))[: length + prefix_len]
			if encrypted == encrypted2:
				known.append(c)
				break
	return bytes(known)


def oracle(s):
	print(s)
	p.sendlineafter(b"Send challenge > ", s)
	return bytes.fromhex(p.recvline().split(b"> ")[1].decode())


print(decrypt_ecb_suffix(oracle))
