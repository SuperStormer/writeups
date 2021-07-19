from utils.crypto.xor import xor
flag = b'0\x02\x04\x02\x1c\\VW]c\x1f]A\x1cX[O&T[\x14Tnh%\x7f\tBQ\x01,;\rCT:R\x13TpQP.V\x1c\x0ff\x14\x06g^\x13<EI1\x02'
orz = b'Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you'
print(xor(xor(xor(flag, orz[:57]), orz[57:57 * 2]), orz[57 * 2:]).decode())
