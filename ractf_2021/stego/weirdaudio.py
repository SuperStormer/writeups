from scipy.io import wavfile as wav
from utils.itertools2 import grouper
rate, data = wav.read("weirdaudio_out.wav")
o = [-12345, -8888, -6969, -1337, 1337, 6969, 8888, 12345]
x = [o.index(c) for c in data if abs(c) > 12]
print(bytes(int("".join(map(str, c)), 8) for c in grouper(x, 3)).decode())
