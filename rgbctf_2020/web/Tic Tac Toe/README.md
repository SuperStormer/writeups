# Tic Tac Toe

Source: [obf.js](./obf.js)

First plug the obfuscated source into [beautifier.io] for initial cleanup. Then, reading through the source, we notice that `_0x532f` is called often with string literals. Replace each instance with the evaled version in the console on the challenge site. Reading the source again, we see this function:

```js
function _0x27cd85(_0x322624) {
	var _0x3a0b35 = {};
	_0x3a0b35["_0x541616"] = function (_0x3da663, _0x57a2d3) {
		return _0x3da663(_0x57a2d3);
	};
	_0x3a0b35["_0x3b0efc"] = "cmdiQ1RGe2g0aDRfajR2NDJjcjFwN19ldjNuNzJfQVIzX2MwMEx9";
	_0x3a0b35["_0x5f0150"] = "You lose. Couldn't beat the master eh? That's tuff";
	var _0x33b11a = _0x3a0b35;
	_0x33b11a["_0x541616"](_0x1993fc, _0x322624["_0x1e32d6"] === _0x36a523 ? _0x33b11a["_0x3b0efc"] : _0x33b11a["_0x5f0150"]);
}
```

Base64 decoding `cmdiQ1RGe2g0aDRfajR2NDJjcjFwN19ldjNuNzJfQVIzX2MwMEx9` gives the flag.

Flag: rgbCTF{h4h4_j4v42cr1p7_ev3n72_AR3_c00L}
