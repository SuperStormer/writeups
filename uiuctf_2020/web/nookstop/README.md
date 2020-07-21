# nookstop

Source: [index.html](./index.html)

First, we try clicking the button with javascript: `document.getElementById("flag").click()`. However, this only gets us a partial flag, so it is not the right solution. Reading the source, we see this line:

```js
console.log("TODO: シークレット_バックエンド_サービスを可能にする");
```

Google translating this produces `Enable Secret_Backend_Service`. Set the `secret_backend_service` cookie to true to receive the flag.

Flag: uiuctf{wait_its_all_cookies?}
