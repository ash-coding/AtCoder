import sys
import io

_INPUT = """\
10000000
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

ans = 0
for k in range(1, n + 1):
    num = n // k
    ans += num * (num + 1) * k // 2

print(ans)