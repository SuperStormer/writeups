import dis
import marshal
import pathlib

for p in pathlib.Path(".").glob("out*"):
	print(p)
	with p.open("rb") as f:
		codeobj = marshal.loads(f.read())
		dis.dis(codeobj)
