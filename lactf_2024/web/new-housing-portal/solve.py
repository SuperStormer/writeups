from fastapi import FastAPI
from fastapi.responses import FileResponse
import asyncio

app = FastAPI()

@app.get("/")
async def main():
	return FileResponse("index.html")

@app.get("/hang")
async def hang():
	await asyncio.sleep(5)
	return ""
