#!/usr/bin/python
# modified from https://github.com/sourcekris/ctf-solutions/blob/master/forensics/google16-for2/solve.py
# tshark.exe -r mouse.pcapng -Y 'usb.endpoint_address== 0x82  and usb.data_len > 0' -2 -Tfields -e btl2cap.payload | sed 's/.\{2\}/&:/g' | cut -d: -f3,4,5,6 > usb.dat

from PIL import Image, ImageDraw
from subprocess import check_output

print("[*] Extracting data from pcap")
with open('usb.dat') as f:
	md = f.read().splitlines()
x = 1000  # origin coords
y = 300

img = Image.new("RGB", (5000, 1500), "white")
dr = ImageDraw.Draw(img)

print("[*] Drawing you a picture!")
for line in md:
	coords = [j if j < 128 else (j - 256) for j in [int(k, 16) for k in line.split(':')]]
	x += coords[1]
	y += coords[2]
	if coords[0] != 0:
		dr.rectangle(((x - 2, y - 2), (x + 2, y + 2)), fill="black")

img.save("out2.png")
