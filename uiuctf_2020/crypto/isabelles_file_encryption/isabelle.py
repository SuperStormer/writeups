from utils.crypto.xor import xor
import string
from utils.misc import rotations

def remove_spice(b):
	return 0xff & ((b >> 1) | (b << 7))

def add_spice(b):
	return 0xff & ((b << 1) | (b >> 7))

def super_secret_encryption(plaintext, password):
	assert (len(password) == 8)  # I heard 8 character long passwords are super strong!
	assert (password.decode("utf-8").isalpha())  # The numbers on my keyboard don't work...
	assert (b"Isabelle" in plaintext)  # Only encrypt files Isabelle has been mentioned in
	ciphertext = bytearray(
		add_spice(c) ^ password[i % len(password)] for i, c in enumerate(plaintext)
	)
	return ciphertext

def super_secret_decryption(ciphertext, password):
	plaintext = bytearray(
		remove_spice(c ^ password[i % len(password)]) for i, c in enumerate(ciphertext)
	)
	return plaintext

with open("blackmail_encrypted", "rb") as f:
	ct = f.read()
	x = bytes(map(remove_spice, ct))
	for i in range(len(x) - 8):
		key = bytes(map(add_spice, xor(x[i:i + 8], b"Isabelle")))
		if all(c in string.ascii_letters.encode() for c in key):
			print(key)
