import itertools
from multiprocessing import Pool

import numpy as np
from scipy.io import wavfile as wf


def try_d0(d0: int, rceps_s, L: int, N: int):
	print(d0)
	for d1 in range(0, L):
		if d0 == d1:
			continue
		out = [None for _ in range(N)]
		for k in range(N):
			if rceps_s[k][d0] >= rceps_s[k][d1]:
				out[k] = "0"
			else:
				out[k] = "1"
		m = N // 8
		s = []
		for x in np.reshape(out[: 8 * m], (m, 8)):
			s.append(chr(int("".join(list(x)), 2)))

		s = "".join(s)
		if "csaw" in s or all(32 <= ord(c) <= 127 for c in s):
			print(s)
			exit()


if __name__ == "__main__":
	sample_rate, data = wf.read("256.wav")
	# L = 256
	N = 256
	L = len(data) // N

	init_d = 0

	print("r:", sample_rate)
	print("d:", len(data))
	print("L:", L)
	print("N:", N)

	xsig = np.reshape(data[: (N * L)], (N, L))
	rceps_s = [np.fft.ifft(np.log(np.abs(np.fft.fft(xsig[k])))) for k in range(N)]

	pool = Pool(processes=16)
	pool.starmap(
		try_d0,
		zip(
			range(init_d, L),
			itertools.repeat(rceps_s),
			itertools.repeat(L),
			itertools.repeat(N),
		),
	)
