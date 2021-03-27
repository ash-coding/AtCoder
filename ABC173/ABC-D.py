import sys
import io

_INPUT = """\
4
2 2 1 3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int, input().split()))

A.sort(reverse = True)
m = A[0]
ans = 0
j = 0
for i in range(n - 1):
    if i % 2 == 0:
        ans += A[j]
        j += 1
    else:
        ans += A[j]

print(ans)