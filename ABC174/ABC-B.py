import sys
import io

_INPUT = """\
20 100000
14309 -32939
-56855 100340
151364 25430
103789 -113141
147404 -136977
-37006 -30929
188810 -49557
13419 70401
-88280 165170
-196399 137941
-176527 -61904
46659 115261
-153551 114185
98784 -6820
94111 -86268
-30401 61477
-55056 7872
5901 -163796
138819 -185986
-69848 -96669
"""
sys.stdin = io.StringIO(_INPUT)

import math
n, d = map(int, input().split())

ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    r = math.sqrt(pow(x, 2) + pow(y, 2))
    if r <= d:
        ans += 1

print(ans)