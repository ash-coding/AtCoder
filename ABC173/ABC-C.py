import sys
import io

_INPUT = """\
6 6 8
..##..
.#..#.
#....#
######
#....#
#....#
"""
sys.stdin = io.StringIO(_INPUT)

h, w, k = map(int, input().split())
c = [[0] * w for _ in range(h)]
c_original = [[0] * w for _ in range(h)]
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == '#':
            c[i][j] = 1
            c_original[i][j] = 1

ans = 0
for i in range(pow(2, h + w)):
    for x in range(h):
        for y in range(w):
            c[x][y] = c_original[x][y]
    for j in range(h + w):
        if j < h and i >> j & 1:
            c[j] = [0] * w
        elif i >> j & 1:
            for x in range(h):
                c[x][j - h - 1] = 0        
    num = 0
    for x in c:
        num += sum(x)
    if num == k:
        ans += 1

print(ans)