# pydis2ctf

Reversing the bytecode using [the python docs](https://docs.python.org/3/library/dis.html#python-bytecode-instructions) as a reference produces the functions in [pydis.py](./pydis.py). Attempting to decrypt `encodedflag.txt` using both methods reveals that `c1` is the right function.

Flag: csictf{T#a+\_wA5_g0oD_d155aSe^^bLy}
