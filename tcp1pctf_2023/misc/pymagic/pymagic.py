#!/usr/bin/env python3
import re

class something_to_do_huh:
	...

eval = eval
print = print
code = input('>>> ')

if not re.findall('[()\'"0123456789 ]', code):
	for k in (b := __builtins__.__dict__).keys():
		b[k] = None
	print(eval(code, {'__builtins__': {}, '_': something_to_do_huh}))
else:
	print("invalid", re.findall('[()\'"0123456789 ]', code))
