def c1(text):
	ret_text = ""
	for i in list(text):
		counter = text.count(i)
		ret_text += chr(2 * ord(i) - len(text))
	return ret_text

def c2(inpString):
	xorKey = "S"
	length = len(inpString)
	for i in range(length):
		inpString = inpString[:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i + 1:]
	return inpString