1. fuck around with pickletools/fickling for a few hours before giving up
2. Patch `os._exit` to NOP, patch `builtins.exec` and `builtins.eval` to dump the code objects and code strings
3. Use pycdc decompilation + reading bytecode disassembly + dumping `globals()` to figure out that it's just solving a sudoku with a weird method of I/O.
4. However, there are still random `plus[x][y] = z + 1` code strings being run, so you can't just plug directly into a sudoku solver.
5. Use fishhook to hook `str.join` and dump all arguments. See "/lib/x86_64-linux-gnu/libc.so.6", "srand", "rand" and guess that it's just doing `srand(time(0))` and `rand() % 9` to generate x, y and z.
6. [`solve.py`](./solve.py)
