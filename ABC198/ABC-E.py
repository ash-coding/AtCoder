import sys
import io

_INPUT = """\
10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
"""
sys.stdin = io.StringIO(_INPUT)

sys.setrecursionlimit(1000000)
n = int(input())
*c, = map(int, input().split())
M = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    M[a].append(b)
    M[b].append(a)

color = [0] * (max(c) + 1)
visited = [0] * n
ans = []

def dfs(u):
    visited[u] = 1
    if color[c[u]] == 0:
        ans.append(u)
    color[c[u]] += 1
    for v in M[u]:
        if visited[v] == 1:
            continue
        dfs(v)
    color[c[u]] -= 1

dfs(0)
ans.sort()
for x in ans:
    print(x + 1)