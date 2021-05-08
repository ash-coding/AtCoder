import sys
import io

_INPUT = """\
5 896 483
228 59
529 310
339 60
78 266
659 391
"""
sys.stdin = io.StringIO(_INPUT)

n, d, h = map(int, input().split())

ans = 0.0
for _ in range(n):
    di, hi = map(int, input().split())
    x = (d * hi - h * di) / (d - di)
    ans = max(ans, x)

print(ans)