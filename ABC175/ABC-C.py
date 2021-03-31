import sys
import io

_INPUT = """\
1000000000000000 1000000000000000 1000000000000000
"""
sys.stdin = io.StringIO(_INPUT)

x, k, d = map(int, input().split())

if abs(x) // d > k:
    ans = abs(abs(x) - k * d)
else:
    if (abs(x) // d - k) % 2 == 0:
        ans = abs(abs(x) - abs(x) // d * d)
    else:
        ans = abs(abs(x) - (abs(x) // d + 1) * d)

print(ans)
