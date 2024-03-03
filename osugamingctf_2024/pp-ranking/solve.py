import re
import base64
from requests import Session

URL = "https://pp-ranking.web.osugaming.lol"
#URL = "http://localhost:8000"
s = Session()

s.post(URL + "/api/register", data={"username": "Stella-rium", "password": "Stella-rium"})

s.post(
	URL + "/api/submit",
	data={
	"osu": open("./solve/Kano - Stella-rium (Kowari) [Extra].osu", "rb").read(),
	"osr": base64.b64encode(open("./solve/edited2.osr", "rb").read())
	}
)

print(re.search(r"osu{.+}", s.get(URL + "/rankings").text).group(0))
