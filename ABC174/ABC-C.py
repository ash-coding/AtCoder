import sys
import io

_INPUT = """\
999983
"""
sys.stdin = io.StringIO(_INPUT)

k = int(input())

ans = -1
s = 7
for i in range(1, k + 1):
    if s % k == 0:
        ans = i
        break
    s = (s * 10 + 7) % k

print(ans)