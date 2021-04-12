import sys
import io

_INPUT = """\
3 4 4
"""
sys.stdin = io.StringIO(_INPUT)

import math
r, x, y = map(int, input().split())

ans = 0
while x*x + y*y > ans*ans*r*r:
    ans += 1
if ans == 1 and x*x + y*y != r*r:
    ans = 2

print(ans)