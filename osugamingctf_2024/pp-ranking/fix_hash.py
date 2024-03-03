import hashlib
from osrparse import Replay

r = Replay.from_path("solve/SuperStormer - Kano - Stella-rium [Extra] (2023-11-16) Osu.osr")
print(r.beatmap_hash)
r.beatmap_hash = hashlib.md5(open("./solve/Kano - Stella-rium (Kowari) [Extra].osu","rb").read()).hexdigest()
print(r.beatmap_hash)
r.write_path("solve/edited2.osr")