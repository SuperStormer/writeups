import itertools
import math
import random

from PIL import Image

im = Image.open("shuffled.png")
dat = list(im.getdata())

indices = list(range(math.ceil(len(dat) / 15)))
r = random.Random()
r.seed(1272)  # length of the generator code
r.shuffle(indices)

# >>> blocks = [dat[i : i + 15] for i in range(0, len(dat), 15)]
# results in the last block being shorter than the rest
# so we need to fix this manually 💀
shorter_block = indices.index(len(dat) // 15) * 15
blocks = []
i = 0
while i < len(dat):
    if i == shorter_block:
        blocks.append(dat[i : i + (len(dat) % 15)])
        i += len(dat) % 15
    else:
        blocks.append(dat[i : i + 15])
        i += 15

new_blocks = [block for _, block in sorted(zip(indices, blocks))]

im2 = Image.new(im.mode, im.size)
im2.putdata(list(itertools.chain(*new_blocks)))
im2.save("shuffled_out.png", format="PNG")
