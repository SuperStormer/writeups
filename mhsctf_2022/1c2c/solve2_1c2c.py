from PIL import Image

img = Image.open("out.png")
pix = img.load()
assert pix is not None

for i in range(img.size[0]):
	for j in range(img.size[1]):
		if i % 4 != 0:
			pix[i, j] = (0, 0, 0)
img.save("out2.png")