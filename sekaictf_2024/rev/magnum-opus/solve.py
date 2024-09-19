import sudokum
from pwnlib.tubes.process import process
from pwnlib.tubes.remote import remote
from utils.all import b64decode, b64encode, bytes_to_long, long_to_bytes

s = remote("magnum-opus.chals.sekai.team", 1337, ssl=True)
# s = process("./magnum_opus.py")
while True:
	inp = s.recvline()
	if inp.startswith(b"Good job"):
		print(s.recvall())
		break
	print(inp)

	p = process("./a.out")  # gcc fuck.c
	rands = [int(c) for c in p.recvall().split()]
	# print(rands)

	decoded = str(bytes_to_long(b64decode(inp))).zfill(81)

	i = 0
	dirg = [[0 for _ in range(9)] for _ in range(9)]
	for x in range(9):
		for y in range(9):
			dirg[x][y] = int(decoded[i])
			i += 1
	# print(decoded, dirg)

	plus = sudokum.solve(dirg)[1]
	for i in range(11):
		x, y, z = rands.pop(0), rands.pop(0), rands.pop(0)
		plus[x][y] = z + 1

	add = [[0 for _ in range(9)] for _ in range(9)]
	for x in range(9):
		for y in range(9):
			if dirg[x][y] == 0:
				add[x][y] = plus[x][y]

	# print(add)
	# print(plus)
	res = b64encode(
		long_to_bytes(int("".join("".join(str(x) for x in row) for row in plus)))
	)
	print(res)
	s.sendlineafter(b"> ", res)
