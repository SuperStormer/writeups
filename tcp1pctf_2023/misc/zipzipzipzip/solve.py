from subprocess import *

for i in range(25000,0,-1):
    password = open('password.txt').read().strip()
    print(password)
    run(f"7z x '-p{password}' -aoa zip-{i}.zip && rm zip-{i}.zip",shell=True)
