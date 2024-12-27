#!/usr/local/bin/python3.13 -S


def die():
	print("Don't be greedy")
	exit(1)


def check_code(code):
	to_check = ["co_consts", "co_names", "co_varnames", "co_freevars", "co_cellvars"]
	for attr in to_check:
		for obj in getattr(code, attr):
			if type(obj) is not str or len(obj) < 5 or obj[:2] + obj[-2:] != "____":
				print(obj)


code = input("Be careful what you wish for: ")
if "\"'" in code:
	die()

code = compile(code, "<string>", "eval")
check_code(code)
print(eval(code, {"__builtins__": {}}))
