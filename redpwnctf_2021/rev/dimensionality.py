with open("dimension", "rb") as f:
	f.seek(0x00002080)
	data = f.read(1331)
	valid = [i - 0x54 for i, c in enumerate(data) if c != 0]
offsets = {"b": -121, "d": 11, "f": 121, "l": -1, "r": 1, "u": -11}

def solve(curr_val=0, curr_chain=None):
	if curr_chain is None:
		curr_chain = []
	if curr_val == 1212:
		return [curr_chain]
	if curr_val not in valid:
		return None
	if len(curr_chain) > 30:
		return None
	#print(curr_val, curr_chain)
	results = []
	for k, v in offsets.items():
		if curr_chain and (v + offsets[curr_chain[-1]]) == 0:
			continue
		val = curr_val + v
		res = solve(val, curr_chain + [k])
		if res is not None:
			results.extend(res)
	if results:
		return results
	return None

for c in solve():  #type: ignore
	print("".join(c))
