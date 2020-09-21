from base64 import b64decode, b64encode

import hashpumpy
import requests

def parse(resp):  #returns data, hash
	return resp.strip().rpartition(" ")[2].split(":")

for key_len in range(1, 50):
	resp = requests.post(
		"http://crypto.chal.csaw.io:5003/new", data={
		"author": "a",
		"note": ""
		}
	).text
	data, hash = parse(resp)
	data = b64decode(data)
	new_hash, new_data = hashpumpy.hashpump(
		hash, data, "&admin=True&access_sensitive=True&entrynum=7", key_len
	)
	new_data = new_data.decode("latin1").encode("unicode-escape")
	print(key_len, new_hash, new_data)
	resp = requests.post(
		"http://crypto.chal.csaw.io:5003/view",
		data={
		"id": b64encode(new_data),
		"integrity": new_hash
		}
	).text
	print(resp)
	if ">:(" not in resp and "Server Error" not in resp:
		print(resp)
		break
