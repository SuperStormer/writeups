import socketio
import asyncio

url = 'https://infinity.chall.pwnoh.io/'
#url = 'http://localhost:1024/'

main = socketio.AsyncClient()
always_answers: dict[str, tuple[socketio.AsyncClient, int]] = {}

@main.event
async def gameState(data):
	if "correctAnswer" in data:
		if main.get_sid() in data["scoreboard"]:
			print("main score:", data["scoreboard"][main.get_sid()])
	else:
		#print(data)
		
		for sio, val in always_answers.values():
			await sio.emit("answer", val)
		
		await asyncio.sleep(2)
		
		dummy = socketio.AsyncSimpleClient()
		await dummy.connect(url)
		data = (await dummy.receive())[1]
		
		win = None
		for sid, v in always_answers.items():
			if sid in data["scoreboard"] and data["scoreboard"][sid] > 0:
				win = v[1]
				break
		await main.emit("answer", win)

@main.event
async def flag(data):
	print(data)
	exit()

async def main_func():
	await main.connect(url)
	
	for i in range(4):
		sio = socketio.AsyncClient()
		await sio.connect(url)
		always_answers[sio.get_sid()] = (sio, i)
	await main.wait()

asyncio.run(main_func())