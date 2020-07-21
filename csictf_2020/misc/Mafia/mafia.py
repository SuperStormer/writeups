from pwn import *
s = remote("chall.csivit.com", 30721)
num_q = 0
curr_max = None
i = 1
while num_q <= 1000 and i <= 300:
	l = 1
	r = 1000001
	final = None
	while l < r and num_q <= 1000:
		m = (l + r) // 2
		num_q += 1
		s.sendline(f"1 {i} {m}")
		resp = s.recvline().strip()
		print(i, m, resp, num_q)
		if resp == b"G":
			l = m
		elif resp == b"L":
			r = m
		else:
			final = m
			break
		if curr_max and r < curr_max:
			break
	if final is not None:
		curr_max = final
		print(curr_max)
	i += 1

s.sendline(f"2 {curr_max}")
print(s.recvall())