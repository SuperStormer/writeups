# uglybash

Source: [cmd.sh](./cmd.sh)

The first part(`${*%c-dFqjfo} e$'\u0076'al`) translates to `eval`. Replace this `eval` with `echo` to get the second script(in [cmd2.sh](./cmd2.sh)). The first part(`"$@" "${@//.WS1=|}" $BASH ${*%%Y#0C} ${*,,}`) translates to `/bin/bash`, meaning the entire script is redirecting the herestring into bash. Replace this with `echo` to get `echo dont just run it, dummy # flag{us3_zsh,_dummy}`.

Flag: flag{us3_zsh,\_dummy}
