import fontforge

f = fontforge.open("font.woff")

for i in f.selection.all():
	try:
		if f[i].glyphname.count("_") > 3:
			print(f[i])
			f[i].width = 10000
	except TypeError:
		pass

f.generate("font.woff")
