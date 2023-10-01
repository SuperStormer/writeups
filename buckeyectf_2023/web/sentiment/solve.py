from fastapi import FastAPI
from fastapi.responses import FileResponse
import asyncio

app = FastAPI()

@app.get("/solve.html")
async def solve():
	return FileResponse("solve.html")

@app.get("/solve2.html")
async def solve2():
	return FileResponse("solve2.html")

@app.get("/solve3.html")
async def solve3():
	return FileResponse("solve3.html")

@app.get("/hang")
async def hang():
	await asyncio.sleep(15000)
	return ""
