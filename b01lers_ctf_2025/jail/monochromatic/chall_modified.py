#!/usr/local/bin/python3
import dis
import gc


def run():
	pass


gc.disable()
inp = bytes.fromhex(input("Bytecode: "))
names = tuple(input("Names: ").split())
if len(inp) > 200:
	print(f"Invalid bytecode {inp}")
if len(names) > 5:
	print(f"Invalid names {names}")
code = run.__code__.replace(co_code=inp, co_names=names)
for inst in dis.Bytecode(code):
	if (
		inst.opname.startswith("LOAD")
		or inst.opname.startswith("STORE")
		or inst.opname.startswith("IMPORT")
	):
		print(f"Invalid op {inst.opname}")
		exit()
run.__code__ = code


def f():
	# quality code :tm:
	for obj in object.__subclasses__():
		if "Sized" in str(obj):
			for obj in obj.__subclasses__():
				if "Collection" in str(obj):
					for obj in obj.__subclasses__():
						if "Mapping" in str(obj):
							for obj in obj.__subclasses__():
								if "MutableMapping" in str(obj):
									print(
										obj,
										id(obj.popitem.__code__.co_code)
										- id(run.__code__.co_code),
									)


f()
run()
