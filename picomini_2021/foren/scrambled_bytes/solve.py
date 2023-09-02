import itertools
from datetime import datetime
from email.utils import parsedate

from scapy.layers.inet import UDP, ICMP
from scapy.packet import Raw
from scapy.utils import rdpcap
import random

def parse_date(s):
	return datetime(*parsedate(s)[:6])

#dt = parse_date("Tue, 23 Feb 2021 01:45:23 GMT")
#dt = parse_date("Sun, 21 Feb 2021 12:12:10 UTC")

p = rdpcap("./capture.pcapng")
packets = [c for c in p[UDP][Raw] if c[UDP].dport == 56742]

dt = datetime.fromtimestamp(int(packets[0].time))
timestamp = int(dt.timestamp())
timestamp -= 200

#for seed in range(timestamp, timestamp + 1000):
for seed in [1614044650]:
	random.seed(seed)
	t = list(range(len(packets)))
	random.shuffle(t)
	"""
	if random.randrange(65536) == 45829:
		print(seed)
		break
	"""
	scrambled = bytearray()
	for packet in packets:
		rand = random.randrange(65536)
		assert packet[UDP].sport == rand
		scrambled.append(packet[Raw].load[0] ^ random.randrange(256))
	print(scrambled)
	out = bytearray(len(scrambled))
	for i, j in enumerate(t):
		out[j] = scrambled[i]
	print(out)
	with open("out.png", "wb") as f:
		f.write(out)
