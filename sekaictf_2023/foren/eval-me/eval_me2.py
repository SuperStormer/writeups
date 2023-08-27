import json
from scapy.all import *

def xor(s, t) -> bytes:
	return bytes(a ^ b for a, b in zip(s, t))

p = rdpcap("capture.pcapng")

d = ""
for packet in p[TCP]:
	if packet[TCP].dport == 30899:
		payload = bytes(packet[TCP].payload)
		if payload:
			d += json.loads(payload.decode().splitlines()[-1])["data"]

key = b"s3k@1_v3ry_w0w"

print(xor(bytes.fromhex(d), key * 10))