# Typeracer

Source: [obf.js](./obf.js)

First plug the obfuscated source into [beautifier.io] for initial cleanup. Then, reading through the source, we notice that `_0x7379` is called often with 2 string literals. Replace each instance with the evaled version in the console on the challenge site. Reading the source again, we see this line:

```js
_0x1c2030: "Congrats y" + "ou have be" + "aten me! H" + "ere's your" + " flag: cmd" + "iQ1RGe3c0M" + "HdfajR2NDJ" + "jcjFwN18xM" + "l80bm4weTF" + "uZ30=",
```

Base64 decoding gives the flag.

Flag: rgbCTF{w40w_j4v42cr1p7_12_4nn0y1ng}
