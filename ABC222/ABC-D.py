import sys
import io

_INPUT = """\
2
1 1
2 3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())
mod = 998244353

m = 3000
dp = [1] * (m + 1)
for i in range(n):
    nx = [0] * (m + 1)
    for j in range(a[i], b[i] + 1):
        nx[j] = dp[j]
    dp = nx
    for i in range(m):
        dp[i + 1] += dp[i]
        dp[i + 1] %= mod
print(dp[m])