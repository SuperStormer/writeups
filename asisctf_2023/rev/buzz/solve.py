import subprocess
import string

flag = "ASIS{"
for i in range(7, 100):
	for c in string.ascii_letters + string.digits + "_~!@#%^&*()+-=}":
		out = subprocess.run(
			[
			"bash", "-c",
			f'diff <(echo "{flag + c}" | ./buzz.elf | head -n {i}) <(head flag.enc -n {i})'
			],
			stdout=subprocess.PIPE,
			check=False
		).stdout
		if not out:
			flag += c
			print(flag)
			break
	else:
		break
