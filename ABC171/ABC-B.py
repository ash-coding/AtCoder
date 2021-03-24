import sys
import io

_INPUT = """\
1 1
1000
"""
sys.stdin = io.StringIO(_INPUT)

n, k = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
ans = 0
for i in range(k):
    ans += p[i]

print(ans)