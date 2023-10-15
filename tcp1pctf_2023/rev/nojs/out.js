const _0x50c61b = _0x14f2;

function _0x14f2(_0x3f3c46, _0x13f40f) {
	const _0x406378 = _0x4063();
	return (
		(_0x14f2 = function (_0x14f219, _0x16d87d) {
			_0x14f219 = _0x14f219 - 0x1a9;
			let _0x122f15 = _0x406378[_0x14f219];
			return _0x122f15;
		}),
		_0x14f2(_0x3f3c46, _0x13f40f)
	);
}

function _0x4063() {
	const _0x46c43d = [
		"940796mTdpEl",
		"question",
		"readline",
		"log",
		"charCodeAt",
		"length",
		"close",
		"fromCharCode",
		"966120xqwCjs",
		"7EgWSxD",
		"3446815bkIcDw",
		"4510464YBSrwE",
		"5680971RIpQtA",
		"13356RBJnMc",
		"Nope.",
		"828688ndmvdt",
		"798eatJjS",
		"\x1a\x01\x0a\x161\x00\x10:\x0f6\x15\x00\x1c\x10<\x09\x01\x07\x04:\x05\x0c\x1a:\x0c\x1c\x17:\x0a\x06\x0d\x111\x0b\x0c\x11\x06\x0c\x11:\x04\x1c\x10\x111\x1c\x10\x001\x00\x17:\x1a\x06<\x02\x0b\x1d<\x11\x06\x0c<\x03\x02\x08\x04",
		"stdout",
		"Enter\x20the\x20secret:\x20",
		"¯\u0091G\u009b±\u009dRÃ\u0099\u009aO\u0095\x1bB\x0eh¶\u009eA*\x00eÉO^\x1c¥K\x11\u009e\u0097\x07",
	];
	_0x4063 = function () {
		return _0x46c43d;
	};
	return _0x4063();
}
(function (_0x5248cc, _0xaf47f9) {
	const _0x2d018f = _0x14f2,
		_0x48ec16 = _0x5248cc();
	while (!![]) {
		try {
			const _0x55c897 =
				parseInt(_0x2d018f(0x1ba)) / 0x1 +
				-parseInt(_0x2d018f(0x1b4)) / 0x2 +
				(parseInt(_0x2d018f(0x1b5)) / 0x3) * (-parseInt(_0x2d018f(0x1b2)) / 0x4) +
				parseInt(_0x2d018f(0x1af)) / 0x5 +
				(parseInt(_0x2d018f(0x1b0)) / 0x6) * (parseInt(_0x2d018f(0x1ae)) / 0x7) +
				parseInt(_0x2d018f(0x1ad)) / 0x8 +
				-parseInt(_0x2d018f(0x1b1)) / 0x9;
			if (_0x55c897 === _0xaf47f9) break;
			else _0x48ec16["push"](_0x48ec16["shift"]());
		} catch (_0x3764d9) {
			_0x48ec16["push"](_0x48ec16["shift"]());
		}
	}
})(_0x4063, 0x8ae63);

function gamma(str1, part1) {
	const _0x116a89 = _0x14f2;
	let _0x222772 = [],
		part1_len = part1["length"];
	for (let i = 0x0; i < 0x100; i++) {
		_0x222772[i] = i;
	}
	let _0x2c72f3 = 0x0;
	for (let j = 0x0; j < 0x100; j++) {
		(_0x2c72f3 = (_0x2c72f3 + _0x222772[j] + part1["charCodeAt"](j % part1_len)) % 0x100),
			([_0x222772[j], _0x222772[_0x2c72f3]] = [_0x222772[_0x2c72f3], _0x222772[j]]);
	}
	let _0x249188 = 0x0;
	_0x2c72f3 = 0x0;
	let _0x5584aa = "";
	for (let _0x48d33d = 0x0; _0x48d33d < str1["length"]; _0x48d33d++) {
		(_0x249188 = (_0x249188 + 0x1) % 0x100),
			(_0x2c72f3 = (_0x2c72f3 + _0x222772[_0x249188]) % 0x100),
			([_0x222772[_0x249188], _0x222772[_0x2c72f3]] = [
				_0x222772[_0x2c72f3],
				_0x222772[_0x249188],
			]);
		const _0x17a471 =
			str1["charCodeAt"](_0x48d33d) ^
			_0x222772[(_0x222772[_0x249188] + _0x222772[_0x2c72f3]) % 0x100];
		_0x5584aa += String["fromCharCode"](_0x17a471);
	}
	return _0x5584aa;
}

function alpha(str) {
	let tot = 0x0;
	if (str["length"] === 0x0) return tot;
	for (let i = 0x0; i < str["length"]; i++) {
		const c = str["charCodeAt"](i);
		(tot = (tot << 0x5) - tot + c), (tot |= 0x0);
	}
	return tot;
}

function xor(str1, input) {
	let out = "";
	for (let i = 0x0; i < str1["length"]; i++) {
		const c = str1["charCodeAt"](i) ^ input["charCodeAt"](i % input["length"]);
		out += String["fromCharCode"](c);
	}
	return out;
}

for (let i = 0; i < 128; i++) {
	for (let j = 0; j < 128; j++) {
		for (let k = 0; k < 128; k++) {
			for (let l = 0; l < 128; l++) {
				const _0x28c214 = _0x50c61b;
				const inp = String.fromCharCode(i, j, k, l);
				if (alpha(inp) == 0x33975d) {
					console.log(inp);
					const part1 = xor(_0x28c214(0x1b6), inp);
					console["log"](gamma(_0x28c214(0x1b9), part1));
				} else {
				}
			}
		}
	}
}
