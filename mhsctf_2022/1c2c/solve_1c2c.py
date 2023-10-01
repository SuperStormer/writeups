from re import A
from PIL import Image

def glorp(n):
	g = list(format(n, "08b"))
	for i in range(len(g)):
		t = g[i]
		g[i] = g[(i * 332 + 6) % 8]
		g[(i * 332 + 6) % 8] = t
	return int(''.join(g), 2)

lookup = [glorp(i) for i in range(256)]

img = Image.open("1c2c.png")
pix = img.load()

assert pix is not None

for i in range(img.size[0]):
	for j in range(img.size[1]):
		pix[i, j] = (
			lookup.index(pix[i, j][0]), lookup.index(pix[i, j][1]), lookup.index(pix[i, j][2])
		)

img.save("out.png")
