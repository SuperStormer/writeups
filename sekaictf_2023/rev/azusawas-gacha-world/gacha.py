import requests
def fetch():
	return requests.post("http://172.86.64.89:3000/gacha",json={"crystals":99999999,"pulls":999999,"numPulls":10},headers={"User-Agent":"SekaiCTF"}).json()

while 1:
	for a in fetch()["characters"]:
		if "flag" in a:
			print(a["flag"])
			exit()
