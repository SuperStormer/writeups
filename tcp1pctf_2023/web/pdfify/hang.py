from fastapi import FastAPI
from fastapi.responses import FileResponse
import asyncio

app = FastAPI()

@app.get("/hang")
async def hang():
	await asyncio.sleep(3)
	return ""
