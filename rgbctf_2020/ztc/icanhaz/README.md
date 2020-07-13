# icanhaz

Source: [icanhaz.xyz](./icanhaz.xyz)

A lot of tedious work.

```
$ mv icanhaz.xyz icanhaz.xz
$ xz -d icanhaz.xz
$ file icanhaz
icanhaz: ASCII text
$ cat icanhaz
00000000: FD37 7A58 5A00 0004  ..:.!...
00000008: E6D6 B446 0200 2101  WO......
00000010: 1600 0000 742F E5A3  ......Vt
00000018: E22C 1D08 A85D 001E  S...y)..
00000020: 0FCB 8711 D8CE 6691  ..g.Q..j
00000028: 0F83 1ECA FD7B 33D4  .c...#.M
00000030: 7FE9 B7DA 2831 7625  "Z......
00000038: 6620 4D2A 096D 6AF7  ..(.._.7
00000040: 2970 3841 1395 088A  .....n..
00000048: D05B 1D93 4BE2 5286  }$.l.S.f
00000050: 850B F72A BFC6 554F  e.7..F.|
00000058: B589 0C70 CE64 EB81  .i.....a
00000060: 1285 58B3 EC81 29EF  .e...a..
00000068: 9E9F F458 0A5A 0D3E  ..4..!..
00000070: 3D52 1C01 30D7 E486  .....PUf
00000078: 52E1 6FD4 91C3 64F8  ..?MjC.8
[...]
$ cat icanhaz | cut -d' ' -f 2,3,4,5 > dump
$ cat dump
FD37 7A58 5A00 0004
E6D6 B446 0200 2101
1600 0000 742F E5A3
E22C 1D08 A85D 001E
0FCB 8711 D8CE 6691
0F83 1ECA FD7B 33D4
7FE9 B7DA 2831 7625
6620 4D2A 096D 6AF7
2970 3841 1395 088A
D05B 1D93 4BE2 5286
850B F72A BFC6 554F
B589 0C70 CE64 EB81
[...]
$ python3
Python 3.8.4rc1 (default, Jul  1 2020, 15:31:45)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> open("dump2","wb").write(bytes.fromhex(open("dump").read()))
2280
>>>
$ file dump2
dump2: XZ compressed data
$ mv du
dump   dump2
$ mv dump2 du
dump   dump2
$ mv dump2 dump2.xz
$ xz -d dump2.xz
$ file dump2
dump2: SVG Scalable Vector Graphics image
$ sed -i "s/#fffffd/#000000/" dump2
$ start dump2
$ mv dump2 dump2.svg
$ start dump2.svg
$ # scan qr code with phone
$ base64 -d
/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4AbxAN1dAA2XxNFhRNBaOJSxhV08AXoOcZxtalpXU+c+q/ppfZc1/t0z3BU/P16F9jAlXbjrzh5cXk/9vLbc+8NQJ8PNawtALEPD17f25zdggODx3xzNLY3SjGTIlX0fbqo6HFkHYkIzOjjUgJcN1KbzGRouW+G8TakjrJ4y5Pk7jv/stqRiV0ICPYxKpnZSEn0aLzQSl46j6H3BBUBhRuGgxue3TXIzw5HGMlchgNBs6SCfHU0SkX4zlSKqOWSyKrJ5JMgwC47en2kI68/tRNQYaYzvGGcWcR/iEgNYO/jHVDVLAAAAADjqmgxrEIjCAAH5AfINAADD+B/oscRn+wIAAAAABFla
���aD�Z8���]<zq�mjZWS�>��i}�5��3�??^��0%]���\^O������P'��k
Ԧ�.[�M�#��2��;��춤bWB=�J�vR}/4����}�@aF���Mr3Ñ�2W!��l� �M�~3�"�9d�*�y$�0-�Ҍdȕ}n�:YbB3:8Ԁ�
                                                                        �ޟ���D�i��gq�X;��T5K8�
����g�YZ$ base64 -d <<<"/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4AbxAN1dAA2XxNFhRNBaOJSxhV08AXoOcZxtalpXU+c+q/ppfZc1/t0z3BU/P16F9jAlXbjrzh5cXk/9vLbc+8NQJ8PNawtALEPD17f25zdggODx3xzNLY3SjGTIlX0fbqo6HFkHYkIzOjjUgJcN1KbzGRouW+G8TakjrJ4y5Pk7jv/stqRiV0ICPYxKpnZSEn0aLzQSl46j6H3BBUBhRuGgxue3TXIzw5HGMlchgNBs6SCfHU0SkX4zlSKqOWSyKrJ5JMgwC47en2kI68/tRNQYaYzvGGcWcR/iEgNYO/jHVDVLAAAAADjqmgxrEIjCAAH5AfINAADD+B/oscRn+wIAAAAABFla" > dump3
$ file dump3
dump3: XZ compressed data
$ mv dump3 dump3.xz
$ xz -d dump3.xz
$ file dump3
dump3: UTF-8 Unicode text, with escape sequences
$ cat dump3
█████████████████████████████████
█████████████████████████████████
████ ▄▄▄▄▄ █▀▀ ███ ▀▀█ ▄▄▄▄▄ ████
████ █   █ █▄▀██▀▀▀ ▀█ █   █ ████
████ █▄▄▄█ █ ▄ █  ▄ ██ █▄▄▄█ ████
████▄▄▄▄▄▄▄█ █ ▀▄█ █▄█▄▄▄▄▄▄▄████
████ ▄▀ ▀▀▄▄▀▀█  ▀   ▀ ▄▄▀▄ ▀████
████▄█▀▄▀▀▄█ ▀▀  ▀▀▀▀▀▄▀▀█▄  ████
████▄ █▀ █▄ ██▄ █▀██▀  ▀▄▀   ████
████▄▀█▄█▄▄ ▄▀█ █ ██▄▀▀ ▀▄█▀ ████
████▄▄▄▄██▄▄▀▀ █ ▄▀▄ ▄▄▄ ▄█▀ ████
████ ▄▄▄▄▄ █▄█▀▄ ▄▀▄ █▄█ █  ▄████
████ █   █ █▀█▄▀▄▀▄█▄▄▄  █▄▄█████
████ █▄▄▄█ █▀▄██▀▀ ▀▀█ █▄█▄█▄████
████▄▄▄▄▄▄▄█▄▄█▄█▄█▄▄█▄██▄█▄▄████
█████████████████████████████████
█████████████████████████████████
$ # scan qr code again with phone
```

Flag: rgbCTF{iCanHaz4N6DEVJOB}
