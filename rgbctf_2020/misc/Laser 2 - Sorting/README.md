# Laser 2 - Sorting

Source: [Quintec/LaserLang](https://github.com/Quintec/LaserLang)

Really awful implementation of insertion sort.

Psuedocode:

```
sorted = []
array = input
while len(array)>0:
	m = min(array)
	output = []
	for el in array:
		if el == m:
			sorted.append(el)
		else:
			output.append(el)
	array = output
print(sorted)
```

Final Exploit: [sort.lsr](./sort.lsr)

Flag: rgbCTF{1_f33l_y0ur_p41n_trust_m3}
