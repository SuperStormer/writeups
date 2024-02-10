hash = bytes.fromhex("5dfd1ac9741873dbb889fc5f6362af39c7e8085ea3d952974f37ca66e6f6c597")
order = [
	4, 3, 29, 20, 25, 30, 28, 5, 16, 0, 19, 9, 7, 15, 13, 21, 18, 10, 26, 8, 17, 2, 31, 12, 14, 23,
	22, 1, 11, 24, 27, 6
]

print(bytes([c[0] for c in sorted(zip(hash, order), key=lambda x: x[1])]).hex())
