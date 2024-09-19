from pwn import *

x = []
for i in range(30):
	s = remote("misc.csaw.io", 3000)
	s.recvline()
	s.recvline()
	for j in range(30):
		s.recvline()
		s.sendline(str(1 if i == j else 0).encode())
	s.recvline()
	a = int(s.recvline())
	print(a)
	x.append(a - 125)  # 125 from the response with 30 0's
print(bytes(x))
