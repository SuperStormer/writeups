#please ignore the awful code quality
import re
import os
from utils.crypto.xor import xor
from utils.itertools2 import grouper
import itertools
lookup = {}
for fn in os.listdir("src"):
	if fn != "Main.java" and fn.endswith("java"):
		matches = re.finditer(
			r"""public String (\w+)\(\) { 
 return "(\w+)";
}""",
			open("src/" + fn).read()
		)
		curr = {}
		for match in matches:
			first_half = match.group(1)
			v = match.group(2)
			curr[first_half] = v
		lookup[fn[:2]] = curr
#print(lookup)
target = grouper("javautil", 2)
possible2 = []

def find(v, x):
	for k2, v2 in v.items():
		if v2 == x:
			yield k2

for x in target:
	x = "".join(x)
	possible = []
	for first_half, v in lookup.items():
		second_halves = list(find(v, x))
		second_halves = itertools.chain.from_iterable(
			find(v, second_half) for second_half in second_halves
		)
		second_halves = itertools.chain.from_iterable(
			find(v, second_half) for second_half in second_halves
		)
		possible.extend(first_half + second_half for second_half in second_halves)
	print(possible)
	possible2.append(possible)
print(possible2)
print(xor(itertools.repeat(2), "".join(p[0] for p in possible2).encode("utf-8")))
