from pwn import *
from math import gcd, factorial
s = remote("chall.csivit.com", 30827)
while True:
	recvd = s.recvline()
	if b"fun()" in recvd:
		print(s.recvall())
		break
	x, y = map(int, recvd.split(b" "))
	send = factorial(gcd(x, y) + 3)
	print(x, y, send)
	s.sendline(str(send))
