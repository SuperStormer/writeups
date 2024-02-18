from fastapi import FastAPI
from fastapi.responses import FileResponse
import asyncio

app = FastAPI()

@app.get("/hang.html")
async def hang_html():
	return FileResponse("hang.html")

@app.get("/")
async def main():
	return FileResponse("index.html")

@app.get("/index2.html")
async def main2():
	return FileResponse("index2.html")

@app.get("/hang")
async def hang():
	await asyncio.sleep(10)
	return ""
