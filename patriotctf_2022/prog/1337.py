from PIL import Image
import itertools
from utils.itertools2 import grouper

def bits_to_int(bits):
	return int("".join(map(str, bits)), 2)

img = Image.open("encoded.png")
pix = img.getdata()
img_bytes = itertools.chain.from_iterable(pix)

bits = []
for pos, byte in zip(itertools.cycle([1, 3, 3, 7]), img_bytes):
	bit = (byte >> (pos - 1)) & 1
	bits.append(bit)

width = bits_to_int(bits[:16])
height = bits_to_int(bits[16:32])
num_channels = bits_to_int(bits[32:34])
print(width, height, num_channels)
bits = bits[34:]
out = Image.new("RGB", (width, height))

print(len(bits))
pixels = []
for rgb in itertools.islice(grouper(grouper(bits, 8), 3), width * height):
	pixel = tuple(map(bits_to_int, rgb))
	pixels.append(pixel)
out.putdata(pixels)
out.save("out.png")
