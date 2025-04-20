import gc

objects = gc.get_objects()

import dis

for obj in objects:
	if hasattr(obj, "__code__") and hasattr(obj.__code__, "co_code"):
		load_index = None
		bytecode = list(dis.Bytecode(obj))
		for i, inst in enumerate(bytecode):
			if inst.opname in ("LOAD_GLOBAL", "LOAD_NAME", "LOAD_FAST"):
				load_index = i
			if inst.opname == "CALL_FUNCTION" and load_index is not None:
				assert inst.arg is not None
				if (
					i - load_index <= 2
					and inst.arg < 2
					and bytecode[i + 1].opname == "CALL_FUNCTION"
				):
					print(
						"found possible",
						obj,
						obj.__module__,
						load_index * 2,
						i * 2,
						inst.arg,
					)
					dis.dis(obj)
				else:
					load_index = None
