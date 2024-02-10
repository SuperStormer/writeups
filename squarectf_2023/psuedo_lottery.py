import requests
import re
from utils.rng.mersenne import *
import socketio

URL = "http://184.72.87.9:8001"
resp = requests.get(URL + "/winning_numbers").text
urls = re.findall(r'a href="([^"]+?)"', resp)
ints = []
for url in urls:
	resp = requests.get(URL + url).text
	ints = list(map(int, re.findall(r'<li>(\d+)</li>', resp))) + ints
print(len(ints))
rand = copy_mersenne_twister(ints)
guess = " ".join(str(rand.rand()) for _ in range(48))

with socketio.SimpleClient() as sio:
	sio.connect("http://184.72.87.9:8001/")
	sio.emit('guess', {"numbers": guess})
	event = sio.receive()
	print(event)
	event = sio.receive()
	print(event)
