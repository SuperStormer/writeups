from z3 import *
a, b, c, d, e = BitVecs("a b c d e", 32)

s = Solver()
for i in range(0, 5):
	cVar1 = d
	a = b >> (c + cVar1 * a & 0x1f)
	cVar2 = e
	b = d << (cVar2 - cVar1 * a & 0x1f)
	c = e >> (a + c * b & 0x1f)
	d = b << (c - cVar1 * cVar2 & 0x1f)
	e = c >> (d + b * cVar2 & 0x1f)
s.add(a + b + c + d + e == 0x7a69)
print(s)
print("solving")
print(s.check())
m = s.model()
print([m.evaluate(c) for c in [a, b, c, d, e]])
import IPython
IPython.embed()