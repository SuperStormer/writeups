from math import ceil, log2

from z3 import UGE, UGT, ULT, BitVec, BV2Int, Concat, Extract, Solver, Sum, ZeroExt


# https://stackoverflow.com/a/61331081
def HW(bvec):
    return Sum(
        [
            ZeroExt(int(ceil(log2(bvec.size()))), Extract(i, i, bvec))
            for i in range(bvec.size())
        ]
    )


def Slice(bvec, r):
    return Concat(*[Extract(i, i, bvec) for i in r])


grid = BitVec("grid", 64)
b0 = Slice(grid, range(0, 8))
b1 = Slice(grid, range(8, 16))
b2 = Slice(grid, range(16, 24))
b3 = Slice(grid, range(24, 32))
b4 = Slice(grid, range(32, 40))
b5 = Slice(grid, range(40, 48))
b6 = Slice(grid, range(48, 56))
b7 = Slice(grid, range(56, 64))
b8 = Slice(grid, range(0, 64, 8))
b9 = Slice(grid, range(1, 64, 8))
b10 = Slice(grid, range(2, 64, 8))
b11 = Slice(grid, range(3, 64, 8))
b12 = Slice(grid, range(4, 64, 8))
b13 = Slice(grid, range(5, 64, 8))
b14 = Slice(grid, range(6, 64, 8))
b15 = Slice(grid, range(7, 64, 8))
b16 = Slice(grid, range(0, 64, 9))
b17 = Slice(grid, range(7, 63, 7))

s = Solver()
s.add(
    ZeroExt(1, Extract(1, 1, grid))
    + ZeroExt(1, Extract(10, 10, grid))
    + ZeroExt(1, Extract(62, 62, grid))
    == 2
)
s.add(UGT(Extract(15, 15, grid), Extract(23, 23, grid)))
s.add(
    ZeroExt(1, Extract(9, 9, grid))
    + ZeroExt(1, Extract(10, 10, grid))
    + ZeroExt(1, Extract(14, 14, grid))
    == 2
)
s.add(
    ZeroExt(3, Extract(26, 26, grid)) << 3
    == ZeroExt(3, Extract(43, 43, grid)) + ZeroExt(3, Extract(44, 44, grid))
)
s.add(
    ULT(
        ZeroExt(2, Extract(32, 32, grid)) + ZeroExt(2, Extract(33, 33, grid)),
        ZeroExt(2, Extract(1, 1, grid)) + ZeroExt(2, Extract(62, 62, grid)),
    )
)

s.add(HW(~(b2 ^ b4)) == 3)

s.add(HW(b6) == 5)
s.add(
    ZeroExt(1, Extract(61, 61, grid))
    + ZeroExt(1, Extract(42, 42, grid))
    + ZeroExt(1, Extract(43, 43, grid))
    == ZeroExt(1, Extract(25, 25, grid))
    + ZeroExt(1, Extract(26, 26, grid))
    + ZeroExt(1, Extract(27, 27, grid))
)
s.add(
    ZeroExt(4, Extract(38, 38, grid))
    + ZeroExt(4, Extract(46, 46, grid))
    + ZeroExt(4, Extract(54, 54, grid))
    + ZeroExt(4, Extract(62, 62, grid))
    + ZeroExt(4, Extract(39, 39, grid))
    + ZeroExt(4, Extract(47, 47, grid))
    + ZeroExt(4, Extract(55, 55, grid))
    + ZeroExt(4, Extract(63, 63, grid))
    == 5
)
s.add((Extract(14, 14, grid) ^ 1 != Extract(15, 15, grid)))
s.add(
    ZeroExt(1, Extract(57, 57, grid))
    + ZeroExt(1, Extract(59, 59, grid))
    + ZeroExt(1, Extract(60, 60, grid))
    == 3
)
s.add(Extract(18, 18, grid) != Extract(23, 23, grid))
s.add(Extract(11, 11, grid) ^ Extract(19, 19, grid) == 1)
s.add(Extract(50, 50, grid) == Extract(51, 51, grid))
s.add(Extract(20, 20, grid) ^ Extract(7, 7, grid) == 1)
s.add((Extract(63, 63, grid) >> 1 != Extract(63, 63, grid) << 1))
s.add(HW(b9 ^ b1) == 2)
s.add(
    ZeroExt(1, Extract(57, 57, grid))
    + ZeroExt(1, Extract(58, 58, grid))
    + ZeroExt(1, Extract(59, 59, grid))
    == 2
)
s.add(Extract(37, 37, grid) | Extract(38, 38, grid) == Extract(2, 2, grid))
s.add(Extract(4, 4, grid) == Extract(48, 48, grid))
s.add(Extract(4, 4, grid) == Extract(49, 49, grid))
s.add(UGE(Extract(17, 17, grid), Extract(30, 30, grid)))
s.add((Extract(0, 0, grid) == Extract(19, 19, grid)))
s.add(
    ZeroExt(1, Extract(26, 26, grid))
    + ZeroExt(1, Extract(28, 28, grid))
    + ZeroExt(1, Extract(29, 29, grid))
    == ZeroExt(1, Extract(51, 51, grid)) << 1
)
s.add(
    ZeroExt(1, Extract(3, 3, grid))
    + ZeroExt(1, Extract(5, 5, grid))
    + ZeroExt(1, Extract(55, 55, grid))
    == 1
)
s.add((Extract(30, 30, grid) == Extract(34, 34, grid)))
s.add(
    HW(Extract(16, 14, grid))
    > ZeroExt(2, Extract(56, 56, grid) + Extract(30, 30, grid) + Extract(47, 47, grid))
)
s.add(Extract(7, 7, grid) != Extract(52, 52, grid))
s.add((b16 >> 2) & 1 == 0)
s.add(Extract(8, 8, grid) == Extract(9, 9, grid))
s.add(HW(b16 ^ b15) == 3)
s.add(Extract(6, 6, grid) ^ Extract(56, 56, grid) == 0)
s.add((HW(Extract(35, 30, grid)) == 3))
s.add(Extract(24, 24, grid) + Extract(40, 40, grid) == Extract(2, 2, grid))
s.add(~(Extract(27, 27, grid) ^ Extract(22, 22, grid)) == -1)
s.add(
    Extract(11, 11, grid) ^ Extract(12, 12, grid) ^ Extract(13, 13, grid)
    == Extract(12, 12, grid)
)
s.add(Extract(12, 12, grid) == Extract(4, 4, grid))
s.add(Extract(31, 31, grid) == Extract(47, 47, grid))
s.add(Extract(47, 47, grid) ^ Extract(46, 46, grid) == 1)
s.add(Extract(10, 10, grid) * 2 == Extract(25, 25, grid) * 2 + Extract(41, 41, grid))

# the challenge doesn't check that the flag is ascii
# so we have to do it manually...
for x in [b2, b9, b15, b16, b7, b4, b10, b12]:
    s.add(BV2Int(x) < 128)
    s.add(BV2Int(x) > 30)

print(s.check())
m = s.model()

grid = [m.evaluate(Extract(i, i, grid)).as_long() for i in range(64)]
b0 = int("".join(str(i) for i in grid[0:8]), 2)
b1 = int("".join(str(i) for i in grid[8:16]), 2)
b2 = int("".join(str(i) for i in grid[16:24]), 2)
b3 = int("".join(str(i) for i in grid[24:32]), 2)
b4 = int("".join(str(i) for i in grid[32:40]), 2)
b5 = int("".join(str(i) for i in grid[40:48]), 2)
b6 = int("".join(str(i) for i in grid[48:56]), 2)
b7 = int("".join(str(i) for i in grid[56:64]), 2)
b8 = int("".join(str(i) for i in grid[0:64:8]), 2)
b9 = int("".join(str(i) for i in grid[1:64:8]), 2)
b10 = int("".join(str(i) for i in grid[2:64:8]), 2)
b11 = int("".join(str(i) for i in grid[3:64:8]), 2)
b12 = int("".join(str(i) for i in grid[4:64:8]), 2)
b13 = int("".join(str(i) for i in grid[5:64:8]), 2)
b14 = int("".join(str(i) for i in grid[6:64:8]), 2)
b15 = int("".join(str(i) for i in grid[7:64:8]), 2)
b16 = int("".join(str(i) for i in grid[0:64:9]), 2)
b17 = int("".join(str(i) for i in grid[7:63:7]), 2)
print(grid)
print(
    (
        "tjctf{"
        + chr(b2)
        + chr(b9)
        + chr(b15)
        + chr(b16)
        + chr(b7)
        + chr(b4)
        + chr(b10)
        + chr(b12)
        + "}"
    )
)


def verify():
    assert grid[1] + grid[10] + grid[62] == 2
    assert grid[15] > grid[23]
    assert grid[9] + grid[10] + grid[14] == 2
    assert grid[26] << 3 == grid[43] + grid[44]
    assert grid[32] + grid[33] < grid[1] + grid[62]
    assert (
        sum(
            int(i) == int(j)
            for i, j in [*zip(format(b2, "#010b"), format(b4, "#010b"))][2:]
        )
    ) == 3
    assert bin(b6).count("1") == 5
    assert grid[61] + grid[42] + grid[43] == grid[25] + grid[26] + grid[27]
    assert (
        grid[38]
        + grid[46]
        + grid[54]
        + grid[62]
        + grid[39]
        + grid[47]
        + grid[55]
        + grid[63]
        == 5
    )
    assert grid[14] ^ 1 != grid[15]
    assert grid[57] + grid[59] + grid[60] == 3
    assert grid[18] != grid[23]
    assert grid[11] ^ grid[19] == 1
    assert grid[50] == grid[51]
    assert grid[20] ^ grid[7] == 1
    assert grid[63] >> 1 != grid[63] << 1
    assert (
        sum(
            int(i) != int(j)
            for i, j in [*zip(format(b9, "#010b"), format(b1, "#010b"))][2:]
        )
    ) == 2
    assert grid[57] + grid[58] + grid[59] == 2
    assert grid[37] | grid[38] == grid[2]
    assert grid[4] == grid[48] == grid[49]
    assert grid[17] >= grid[30]
    assert grid[0] == grid[19]
    assert grid[26] + grid[28] + grid[29] == grid[51] << 1
    assert grid[3] + grid[5] + grid[55] == 1
    assert grid[30] == grid[34]
    assert sum(grid[14:17]) > grid[56] + grid[30] + grid[47]
    assert grid[7] != grid[52]
    assert (b16 // 4) % 2 == 0
    assert grid[8] == grid[9]
    assert (
        sum(
            int(i) != int(j)
            for i, j in [*zip(format(b16, "#010b"), format(b15, "#010b"))][2:]
        )
    ) == 3
    assert grid[6] ^ grid[56] == 0
    assert sum(grid[30:36]) == 3
    assert grid[24] + grid[40] == grid[2]
    assert ~(grid[27] ^ grid[22]) == -1
    assert grid[11] ^ grid[12] ^ grid[13] == grid[12] == grid[4]
    assert grid[31] == grid[47]
    assert grid[47] ^ grid[46] == 1
    assert grid[10] * 2 == grid[25] * 2 + grid[41]


verify()
