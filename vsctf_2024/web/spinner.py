import json

import websocket

s = websocket.create_connection("wss://spinner.vsc.tf/ws")


def send(p):
	s.send(json.dumps(p))
	# print(s.recv())


offset = 0
while True:
	send({"x": offset, "y": offset, "centerX": 500, "centerY": 500})
	send({"x": 1000 + offset, "y": offset, "centerX": 500, "centerY": 500})
	send({"x": 1000 + offset, "y": 1000 + offset, "centerX": 500, "centerY": 500})
	send({"x": offset, "y": 1000 + offset, "centerX": 500, "centerY": 500})
	offset += 0.01
	resp = s.recv()
	if "vsctf" in resp:
		print(resp)
		break
