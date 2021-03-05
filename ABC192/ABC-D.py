import sys
import io

_INPUT = """\
100000000000000000000000000000000000000000000000000000000000
1000000000000000000
"""
sys.stdin = io.StringIO(_INPUT)

x = str(input())
m = int(input())

d = 0
for i in x:
    d = max(int(i), d)

n = len(x)
res = 0
left = d
right = m + 1
while left + 1 < right:
    res = 0
    mid = (left + right) // 2
    for i in range(n):
        res += int(x[-(i + 1)]) * (mid ** i)
    if res <= m:
        left = mid
    else:
        right = mid
ans = left - d

if n == 1 and int(x) <= m:
    ans = 1
elif n == 1 and int(x) > m:
    ans = 0

print(ans)