# panda-facts

Source: [index.js](index.js)

```js
async function generateToken(username) {
	const algorithm = "aes-192-cbc";
	const key = Buffer.from(process.env.KEY, "hex");
	// Predictable IV doesn't matter here
	const iv = Buffer.alloc(16, 0);

	const cipher = crypto.createCipheriv(algorithm, key, iv);

	const token = `{"integrity":"${INTEGRITY}","member":0,"username":"${username}"}`;

	let encrypted = "";
	encrypted += cipher.update(token, "utf8", "base64");
	encrypted += cipher.final("base64");
	return encrypted;
}
```

The code generates tokens by building up a JSON object manually via string concatenation. This means that we can inject properties into the JSON through the username, since JSON duplicate keys take the value of the last key.

Final Exploit: `","member":1,"a":"`

Flag: `flag{1_c4nt_f1nd_4_g00d_p4nd4_pun}`
