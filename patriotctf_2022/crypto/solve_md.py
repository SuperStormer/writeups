import requests
#from utils.crypto.hash import sha1_hash_extension
import itertools
from utils.itertools2 import grouper
from utils.crypto.xor import xor
from utils.crypto.hash import sha1, sha1_padding

cookie = "61646d696e3d46616c7365.4f27f46ddf6aa485c5192fdd5b216ae8d8b63817"
user_hex = cookie.split(".")[0]
user = bytes.fromhex(user_hex)
cookie_mac = cookie.split(".")[1]

orig_msg = user
print(orig_msg)
new_msg = b"=True"

def sha1_hash_extension(orig_msg, new_msg, oracle, key_lens=None):
	orig_hash = bytes.fromhex(cookie_mac)
	if key_lens is None:
		key_lens = itertools.count(1)
	for key_len in key_lens:
		glue_padding = sha1_padding(b"\x00" * key_len + orig_msg)[key_len + len(orig_msg):]
		msg_added_len = key_len + len(orig_msg) + len(glue_padding)
		state = [int.from_bytes(c, byteorder="big") for c in grouper(orig_hash, 4)]
		forged_mac = sha1(new_msg, state, msg_added_len)
		forged_msg = orig_msg + glue_padding + new_msg
		if oracle(forged_msg, forged_mac):
			break
	raise ValueError("No key_len is valid")

def oracle(forged_msg, forged_mac):
	auth = forged_msg.hex() + "." + forged_mac.hex()
	print(auth)
	resp = requests.get("http://chal2.pctf.competitivecyber.club:49443/", cookies={"auth": auth})
	if "Nothing here yet, but great things are planned!" not in resp.text:
		print(auth)
		print(resp.text)

sha1_hash_extension(orig_msg, new_msg, oracle)
