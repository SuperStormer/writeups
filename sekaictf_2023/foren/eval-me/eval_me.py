from pwn import *

s = remote("chals.sekai.team", 9000)
s.recvlines(4)
while True:
	x = s.recvline()
	print(x)
	s.sendline(str(eval(x)))
	s.recvline()