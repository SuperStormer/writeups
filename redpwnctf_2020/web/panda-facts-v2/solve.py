import base64
import itertools
import random
import string

import requests

while True:
	URL = "https://panda-facts-v2.2020.redpwnc.tf"
	#URL = "http://localhost:3000"
	prefix = '{"integrity":"d2068b64517a277e481166b9b488f593","member":0,"username":"'
	padding = "A" * (80 - 71)
	#junk = "B"*16
	junk = "".join(random.choices(string.ascii_letters, k=16))
	to_be_replaced = "B" * (16 - 2)
	username = padding + junk + to_be_replaced
	token = requests.post(URL + "/api/login", json={"username": username}).json()["token"]
	#actual bit flip code starts here
	initial = bytearray(base64.b64decode(token))
	current = b"B" * (16 - 2) + b"\"}"
	target = b'","member":1}'
	target = b"B" * (16 - len(target)) + target
	for i, c1, c2 in zip(itertools.count(), current, target):
		differences = c1 ^ c2
		initial[80 + i] ^= differences
	new_token = base64.b64encode(initial)
	success = requests.get(URL + "/api/validate", cookies={
		"token": new_token.decode("utf-8")
	}).json()["success"]
	print(success)
	if success:
		print(new_token)
		break
