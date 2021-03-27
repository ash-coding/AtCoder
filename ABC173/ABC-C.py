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
c = [input() for _ in range(h)]

ans = 0
for ic in range(1 << h):
    for jc in range(1 << w):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if ic >> i & 1:
                    continue
                if jc >> j & 1:
                    continue
                if c[i][j] == '#':
                    cnt += 1
        if cnt == k:
            ans += 1

print(ans)