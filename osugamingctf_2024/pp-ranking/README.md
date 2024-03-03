## pp-ranking

The idea is to get the pp of our submitted play to be `Infinity`. This bypasses the anticheat as `parseInt(newPP);` (on line 4 of `anticheat.js`) becomes NaN, which always compares false against any other value.

After some fruitless efforts spent reading the source code of https://github.com/kionell/osu-standard-stable/ and testing Aspire maps, I stumbled upon a way to get the pp to be Infinity by editing a map (in this case, [Kano - Stella-rium [Extra]](https://osu.ppy.sh/beatmapsets/1107950#osu/2315560))'s difficulty values: 
```
[Difficulty]
HPDrainRate:100000
CircleSize:100000000
OverallDifficulty:1000000
ApproachRate:10000
SliderMultiplier:1.65
SliderTickRate:1
```

Now all that needs to be done is modifying the beatmap hash of the replay file to match the updated map using osrparse (see [`fix_hash.py`](./fix_hash.py)) and we can submit for the flag (see [`solve.py`](./solve.py)).
