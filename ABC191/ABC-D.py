import sys
import io

_INPUT = """\
0.2 0.8 1.1
"""
sys.stdin = io.StringIO(_INPUT)

import math
x, y, r = map(float, input().split())

k = 10000
x = round(x * k)
y = round(y * k)
r = round(r * k)

xmin = (x - r) // k
xmax = (x + r) // k

ans = 0
for i in range(xmin, xmax + 1):
    p2 = pow(r, 2) - pow(i * k - x, 2)
    if p2 < 0:
        continue
    p = math.isqrt(p2)
    ymin = (y - p - 1) // k
    ymax = (y + p) // k
    ans += (ymax - ymin)

print(ans)
