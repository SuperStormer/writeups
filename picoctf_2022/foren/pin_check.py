import subprocess
import string
import time

prev = ""
for _ in range(8):
	times = []
	for c in range(10):
		inp = (prev + str(c)).ljust(8, "0")
		start = time.perf_counter_ns()
		subprocess.run("./pin_checker", input=inp.encode(), stdout=subprocess.DEVNULL)
		end = time.perf_counter_ns()
		times.append((end - start, c))
	print(max(times))
	prev += str(max(times)[1])
print(prev)
subprocess.run("./pin_checker", input=prev.encode())
subprocess.run("nc saturn.picoctf.net 53639", shell=True, input=prev.encode())
