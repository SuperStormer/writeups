# Penguins

Source: [git/](./git)

`git reflog` shows `57adae7 HEAD@{2}: commit: relevant file`. Checking out `57adae7` reveals a `perhaps_relevant_v2` file with these contents:

`YXMgeW9kYSBvbmNlIHRvbGQgbWUgInJld2FyZCB5b3UgaSBtdXN0IgphbmQgdGhlbiBoZSBnYXZlIG1lIHRoaXMgLS0tLQpyZ2JjdGZ7ZDRuZ2wxbmdfYzBtbTE3c180cjNfdU5mMHI3dW40NzN9`

Base64 decoding produces the flag.

Flag: rgbctf{d4ngl1ng_c0mm17s_4r3_uNf0r7un473}
