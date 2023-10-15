import requests
from io import BytesIO
from utils.rng.mersenne import copy_mersenne_twister  # https://github.com/SuperStormer/pyutils/blob/master/utils/rng/mersenne.py
from utils.all import long_to_bytes, bytes_to_long, xor

def copy_mersenne_twister3(n):
	"""from the result of random.getrandbits(624 * 32)"""
	vals = []
	while n > 0:
		vals.append(n & ((1 << 32) - 1))
		n >>= 32
	return copy_mersenne_twister(vals)

resp = requests.post(
	"http://ctf.tcp1p.com:54734/", files={
	"file": ("a.txt", BytesIO(bytes(624 * 4)))
	}
).content

r = copy_mersenne_twister3(bytes_to_long(resp))

ct = requests.get("http://ctf.tcp1p.com:54734/flago").content

key = long_to_bytes(r.to_random().getrandbits(len(ct) * 8))
pt = xor(ct, key)
open("out.jpg", "wb").write(pt)