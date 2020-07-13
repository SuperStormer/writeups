# panda-facts-v2

Source: [index.js](./index.js)

```js
async function generateToken(username) {
	const algorithm = "aes-192-cbc";
	const key = Buffer.from(process.env.KEY, "hex");
	// Predictable IV doesn't matter here
	const iv = Buffer.alloc(16, 0);

	const cipher = crypto.createCipheriv(algorithm, key, iv);

	const token = {
		integrity: INTEGRITY,
		member: 0,
		username: username,
	};

	let encrypted = "";
	encrypted += cipher.update(JSON.stringify(token), "utf8", "base64");
	encrypted += cipher.final("base64");
	return encrypted;
}
```

We can see that the token is generated with AES using the CBC mode. This is vulnerable to CBC bit-flipping, where introducing an error in one block will cause the corresponding error in the following block. The username will be composed of 3 parts. The 1st part will be padding in order for the next two parts to occupy an entire block. The 2nd part will be the actual block in which we introduce errors. The 3rd block will be the block that will be changed into `"member":1` plus padding. Using this, we can craft a solve script to generate a valid token.

Final Exploit: [solve.py](./solve.py)

Flag: `flag{54v3_th3_b335_1n5t34d}`
