# HTB 0x2

nmap reveals an open ssh port and a http server on port 3000 running on Express. This brings us to a login page, which will tell you `No user with username: asdf and password: asdf.` upon entering an incorrect password. Trial and error reveals that the login page is vulnerable to a Blind NoSQL injection, which we use to read the admin password. After logging in, going to `/admin` gives us the flag in the source code.

Script: htb2.py

Flag: csictf{n0t_4ll_1nj3ct10n5_4re_SQLi}
