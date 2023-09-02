import itertools
from utils.crypto.xor import xor

def encrypt(ptxt, key):
	ctxt = b''
	for i in range(len(ptxt)):
		a = ptxt[i]
		b = key[i % len(key)]
		ctxt += bytes([a ^ b])
	return ctxt

with open("output.txt") as f:
	ciphertext = bytes.fromhex(f.read())
random_strs = [
	b'my encryption method',
	b'is absolutely impenetrable',
	b'and you will never',
	b'ever',
	#b'ever',b'ever', b'ever', b'ever', b'ever',
	b'break it'
]
for combo in itertools.product([False, True], repeat=len(random_strs)):
	keys = [s for s, val in zip(random_strs, combo) if val]
	temp = ciphertext
	for k in reversed(keys):
		temp = encrypt(temp, k)
	print(xor(temp, b"Africa!" * 100))
