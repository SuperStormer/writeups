import itertools

def check1(param1):
	ret = 0
	for i in range(1, 17, 2):
		ret = (param1[i] | ~ret) * 2 + (param1[i] ^ ret) + ~ret * -2
	return ret

def check2(param1):
	i = 0
	ret = 0
	while i < len(param1):
		x = param1[i] * 2
		if 0 < (
			~(x ^ 0xfffffff7) * 2 + (~x & 0xfffffff7) * 3 + (x & 8) * 3 + ~(x & 0xfffffff7) * -2
		):
			x = (x // 10 & x % 10) * 2 + (x // 10 ^ x % 10)
		ret += x
		i = (i & 0xfffffffd) * 2 + (4 - (i ^ 2))
	return ret

for i in itertools.product([1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=16):
	if (check1(i) + check2(i)) % 10 == 0:
		print("".join(map(str, i)))
		break
