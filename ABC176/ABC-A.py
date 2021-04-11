import sys
import io

_INPUT = """\
1000 1 1000
"""
sys.stdin = io.StringIO(_INPUT)

n, x, t = map(int, input().split())

if n % x == 0:
    ans = (n // x) * t
else:
    ans = ((n // x) + 1) * t
print(ans)