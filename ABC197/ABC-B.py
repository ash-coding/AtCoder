import sys
import io

_INPUT = """\
5 5 4 2
.#..#
#.###
##...
#..#.
#.###
"""
sys.stdin = io.StringIO(_INPUT)

h, w, x, y = map(int, input().split())
s = []
for _ in range(h):
    c = input()
    s.append(c)

x -= 1
y -= 1

ans = 0
i = x
while i >= 0:
    if s[i][y] == '.':
        ans += 1
        i -= 1
    else:
        break
i = x
while i <= h - 1:
    if s[i][y] == '.':
        ans += 1
        i += 1
    else:
        break
j = y
while j >= 0:
    if s[x][j] == '.':
        ans += 1
        j -= 1
    else:
        break
j = y
while j <= w - 1:
    if s[x][j] == '.':
        ans += 1
        j += 1
    else:
        break
print(ans - 3)