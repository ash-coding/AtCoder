import sys
import io

_INPUT = """\
5 7
.......
.###...
.#...#.
.#####.
.......
"""
sys.stdin = io.StringIO(_INPUT)

h, w = map(int, input().split())
s = []
for _ in range(h):
    string = input()
    s.append(string)

ans = 0
left = [[] for _ in range(h)]
right = [[] for _ in range(h)]
for i in range(1, h):
    if s[i] == '.' * w:
        continue
    for j in range(1, w - 1):
        if s[i][j] == '#' and s[i][j - 1] != '#':
            left[i].append(j)
            if j not in left[i - 1]:
                ans += 2
        if s[i][j] == '#' and s[i][j + 1] != '#':
            right[i].append(j)
            if j not in right[i - 1]:
                ans += 2

print(ans)