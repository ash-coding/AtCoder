import sys
import io

_INPUT = """\
4
20 11 9 24
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int, input().split()))

s = 0
for a in A:
    s ^= a

ans = []
for i in range(n):
    x = A[i] ^ s
    ans.append(x)

print(*ans)
