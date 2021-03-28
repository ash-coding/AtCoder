import sys
import io

_INPUT = """\
3
10 10 10
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int, input().split()))

ans = 0
for x in A:
    ans ^= x

for i in range(1, pow(2, n - 1)):
    ored = A[-1]
    xored = 0
    for j in range(n - 1):
        if i >> j & 1:
            xored ^= ored
            ored = A[- j - 2]
        else:
            ored |= A[- j - 2]
    xored ^= ored
    if xored < ans:
        ans = xored

print(ans)
