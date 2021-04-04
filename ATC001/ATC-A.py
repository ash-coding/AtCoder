import sys
import io

_INPUT = """\
4 4
...s
....
....
.g..
"""
sys.stdin = io.StringIO(_INPUT)

sys.setrecursionlimit(1000000)
h, w = map(int, input().split())
c = ['#' * (w + 2)]
for _ in range(h):
    c.append('#' + input() + '#')
c.append('#' * (w + 2))

for x in range(h + 2):
    for y in range(w + 2):
        if c[x][y] == 's':
            si = x
            sj = y
        if c[x][y] == 'g':
            gi = x
            gj = y

visited = [[0] * (w + 2) for _ in range(h + 2)]

def dfs(i, j):
    if c[i][j] == '#':
        return
    if visited[i][j] == 1:
        return
    visited[i][j] = 1
    if visited[i + 1][j] != 1 and c[i + 1][j] != '#':
        dfs(i + 1, j)
    if visited[i][j + 1] != 1 and c[i][j + 1] != '#':
        dfs(i, j + 1)
    if visited[i - 1][j] != 1 and c[i - 1][j] != '#':
        dfs(i - 1, j)
    if visited[i][j - 1] != 1 and c[i][j - 1] != '#':
        dfs(i, j - 1)

dfs(si, sj)

if visited[gi][gj] == 1:
    print('Yes')
else:
    print('No')