import asyncio

from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/hang/{name}")
async def hello(request):
	await asyncio.sleep(10000)
	return web.Response(text="Hung")


app = web.Application()
app.add_routes(routes)
web.run_app(app)
