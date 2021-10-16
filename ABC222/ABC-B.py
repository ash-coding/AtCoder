import sys
import io

_INPUT = """\
2 22
6 37
"""
sys.stdin = io.StringIO(_INPUT)

n, p = map(int, input().split())
*A, = map(int, input().split())

ans = 0
for a in A:
    if a < p:
        ans += 1

print(ans)