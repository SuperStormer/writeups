buf = list("eyrnou jngkiaccre af suryot arsto  tdyea rre aou" + "\x00" * 100)

for k in range(0, 0x30, 2):
	buf[k], buf[k + 1] = buf[k + 1], buf[k]

for j in range(0x31, -1, -1):
	buf[j], buf[j + 1] = buf[j + 1], buf[j]

inp = ["" for _ in range(100)]
for i in range(0x18, -1, -1):
	cVar1 = buf[0x31 - i]
	inp[(0x32 - i) + -1] = buf[i]
	inp[i] = cVar1

print("".join(inp))
