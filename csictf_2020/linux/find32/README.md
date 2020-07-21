# find32

Grepping for `csictf` produces `csictf{not_the_flag}{user2:AAE976A5232713355D58584CFE5A5}` plus other junk. Looking through the filesystem, we see a `/user2` directory, that we can enter by running `su user2` and entering the password. Listing the files with `ls -la` reveals that `sadsas.tx` is one line longer than the rest. `diff sadsas.tx adgsfdgasf.d` produces `th15_15_unu5u41`, which we wrap in flag format.

Flag: csictf{th15_15_unu5u41}
