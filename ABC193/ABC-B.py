import sys
import io

_INPUT = """\
3
5 9 5
6 8 5
7 7 5
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

ans = 1000000005
t = 0
for _ in range(n):
    a, p, x = map(int, input().split())
    t = a
    if x - t > 0:
        ans = min(ans, p)

if ans > 1000000000:
    print(-1)
else:
    print(ans)