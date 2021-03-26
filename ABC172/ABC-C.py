import sys
import io

_INPUT = """\
3 4 730
60 90 120
80 150 80 150
"""
sys.stdin = io.StringIO(_INPUT)

import bisect
n, m, k = map(int, input().split())
A =list(map(int, input().split()))
B =list(map(int, input().split()))

Bacc = [0] * m
b = 0
for i in range(m):
    b += B[i]
    Bacc[i] = b

a = 0
ans = bisect.bisect_right(Bacc, k)
for i in range(n):
    a += A[i]
    time = k - a
    if time < 0:
        break
    Bind = bisect.bisect_right(Bacc, time)
    num = Bind + i + 1
    if num > ans:
        ans = num
    
print(ans)