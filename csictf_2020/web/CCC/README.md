# CCC

The `/adminNames` link first redirects to `/getFile?file=admins` which then leads us to a github repo which contains a list of usernames. Keep this in mind, as this will be used later. The login page lets us enter any random username/password combo, and gives us a JWT token in return. The JWT token has 3 properties: `username`, `password` and `admin`, all ROT-13 encoded. It is now clear what the exploit should be: we need to grab the JWT secret key and forge a JWT token with an `"admin":true` property. We can read the environment variables with `/getFile?file=../.env`, which gives us the JWT secret key: `Th1sSECr3TMu5TN0Tb3L43KEDEv3RRRRRR!!1`. Forge a JWT token using `jwt_tool.py` and use it to enter the `/admin` path, which gives us the flag.

Flag: csictf{1n_th3_3nd_1t_d0esn't_3v3n_m4tt3r}
