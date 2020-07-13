# PI 1: Magic in the air

Source: [data](./data)

The file provided is a BTSnoop file, so we open it in Wireshark. According to my [teammate](https://github.com/AC01010/), this is for a Bluetooth keyboard and the relative packets are the `Rcvd Handle Value Notification` ones. We can extract the packet values with tshark:

`tshark -r data -Y "btatt.opcode==0x1b" -Tfields -e btatt.value | sed 's/../:&/g2' > bt_dump`

Hmmm, bluetooth is similar enough to usb, lets modify a [usb keyboard parser](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser). Tweak the script to read from the right bytes. Running the script produces this output:

```
yoo man
sorrry for thhe delay  lol

tryiinng to geet  thhis  keybboard workiinnnn

yeeaa  its  nneew. wireless man.

beeen mmovviinng  pproduct

sspeaakiinnn  of yoou nneeded too ccoonntaact  mmy  boy right/

ye

shoouldd  bbe ffiine just ssaay johnny h sent yoou

alrighht lemme geet yoouu  thee  numbeer

hhold uup i''mm  loookiingg forr  it


itss  hhiss  bburner,, gott  iit wwritttenn downn ssoommewhere


yeeahh got it

00736727859

miind it  is aa sswwwedishh nnumbeer. he ggot  it  oonn hhollidaay theere ffeww  mmoonthhs  bbacck

yeahh yoouu can buuy  bburnneers ssuupper eaasiily theere

aalrighht g

yeeaah  its  donny l

rremembeer to tell hiimm i sent yoou

peeace
```

Take the phone number(00736727859) and replace the 1st 2 digits with 46(swedish country code) to get the flag.
Final Exploit: [parse_bt.py](./parse_bt.py)

Flag: rgbCTF{+46736727859}
