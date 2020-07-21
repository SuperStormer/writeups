import random
import sys
import string

key1 = "xtfsyhhlizoiyx"
key2 = "eudlqgluduggdluqmocgyukhbqkx"
flag = "lvvrafwgtocdrdzfdqotiwvrcqnd"
"""
key1 = "zzmlvlpyovlpty"
key2 = "jalivmasvvtbtpjfleoxdiomjhjw"
flag = "vovddgonrarrgtrftrovgdvcvwqq"
"""
map_ = [
	'v', 'r', 't', 'p', 'w', 'g', 'n', 'c', 'o', 'b', 'a', 'f', 'm', 'i', 'l', 'u', 'h', 'z', 'd',
	'q', 'j', 'y', 'x', 'e', 'k', 's'
]

def enc1(text):
	n = random.randint(0, sys.maxsize % 28)
	return text[n:] + text[:n]

def enc2(text):
	temp = ''
	for i in text:
		temp += map_[ord(i) - ord('a')]
	return temp

def dec2(text):
	return "".join(chr(map_.index(c) + ord("a")) for c in text)

key1 = list(key1)
key2 = dec2(key2)
k = key2[:14]
key2 = list(key2[14:])
for i in range(14):
	x = ord(key2[i]) - ord(k[i]) + ord("a")
	if chr(x) in string.ascii_lowercase:
		key2[i] = chr(x)
	else:
		key2[i] = chr((x - 97) % 122)

def decode2(flag, key1, key2):
	for j in range(2):
		for i in range(27, 13, -1):
			temp2 = key2[(ord(key1[i - 14]) - ord('a')) % 14]
			key2[(ord(key1[i - 14]) - ord('a')) % 14] = key2[i - 14]
			key2[i - 14] = temp2
			temp1 = flag[(ord(key2[i - 14]) - ord('a')) % 28]
			flag[(ord(key2[i - 14]) - ord('a')) % 28] = flag[i]
			flag[i] = temp1
		for i in range(13, -1, -1):
			temp2 = key1[(ord(key2[i]) - ord('a')) % 14]
			key1[(ord(key2[i]) - ord('a')) % 14] = key1[i]
			key1[i] = temp2
			temp1 = flag[(ord(key1[i]) - ord('a')) % 28]
			flag[(ord(key1[i]) - ord('a')) % 28] = flag[i]
			flag[i] = temp1
	flag = ''.join(flag)
	return flag

decoded = []
for i in range(28):
	flag2 = dec2(flag[i:] + flag[:i])
	key1_ = key1[:]
	key2_ = key2[:]
	decoded.append(decode2(list(flag2), key1_, key2_))
for i in range(28):
	flag2 = dec2(flag[i:] + flag[:i])
	key1_ = key1[:]
	key2_ = key2[:]
	decoded.append(decode2(list(flag2), key2_, key1_))
for dec in decoded:
	if "csi" in dec:
		dec = dec[dec.index("csi"):] + dec[:dec.index("csi")]
		print(dec)