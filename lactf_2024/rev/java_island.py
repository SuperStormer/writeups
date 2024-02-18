from hashlib import sha256
from itertools import product

x = [
	69, 70, -81, -117, -10, 109, 15, 29, 19, 113, 61, -123, -39, 82, -11, -34, 104, -98, -111, 9,
	43, 35, -19, 22, 52, -55, -124, -45, -72, -23, 96, -77
]
y = [256 + c if c < 0 else c for c in x]
print(y)
for c in product("dp", repeat=8):
	h = sha256()
	h.update("".join(c).encode())
	if h.digest() == bytes(y):
		print("".join(c))
