from ctypes import *

libc = CDLL("libc.so.6")
libc.srand(0)

target = "cioerosgaenessT   ns k urelh oLdTie heri nfdfR"
inp = list(range(46))

i = 0x2D
while i != 0:
	iVar3 = libc.rand()
	cVar1 = inp[i]
	inp[i] = inp[iVar3 % 0x2E]
	inp[iVar3 % 0x2E] = cVar1
	i -= 1

print("".join([c for i, c in sorted(zip(inp, target))]))
