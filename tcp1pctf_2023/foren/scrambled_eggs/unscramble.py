from zlib import crc32
from struct import unpack, pack

png = open('scrambled.png', 'rb').read()

chunk_types = [b"IHDR", b"PLTE", b"IDAT", b"IEND"]

chunks = []
while png:
	# read all of the data up to the next chunk type header
	chunk_type, index = min(
		(
		(chunk_type, c if (c := png.find(chunk_type)) != -1 else len(png))
		for chunk_type in chunk_types
		),
		key=lambda x: x[1]
	)
	
	# didn't feel like special casing the PNG header lol
	chunk_data = png[:index].replace(b'\x89PNG\r\n\x1a\n', b'')
	chunk_size = png[index + 4:index + 8][::-1]
	assert unpack('>I', chunk_size)[0] == len(chunk_data)
	
	crc = crc32(chunk_type + chunk_data)
	
	chunks.append(chunk_size + chunk_type + chunk_data + crc.to_bytes(4, byteorder="big"))
	png = png[index + 8:]

chunks2 = []
while chunks:
	chunks2.append(chunks.pop(0))
	chunks = chunks[::-1]

out = b'\x89PNG\r\n\x1a\n' + b"".join(chunks2[::-1])
open("out.png", "wb").write(out)
