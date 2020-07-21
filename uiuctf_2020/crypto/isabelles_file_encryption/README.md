# isabelles_file_encryption

Source: [super_secret_encryption.py](./super_secret_encryption.py)

The first thing we notice is that remove_spice and add_spice are just bitwise rotates. The current decryption method is `remove_spice(ct^key)`, which can be rearranged to `add_spice(remove_spice(ct)^key)`. By doing this, we can crib drag with the known plaintext of `Isabelle` and print any matches that are all letters. The key ends up being `iSaBelLE`, which we can use to decrypt the file. The decrypted file is a JPG with plaintext in the middle, which we can extract with `strings`.

Script: [isabelle.py](./isabelle.py)

Flag: uiuctf{winner_winner_raccoon_dinner}
