import sys
import io

_INPUT = """\
5
2 1 5 4 3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
*A, = map(int, input().split())

ans = 0
fore = A[0]
for i in range(1, n):
    cur = A[i]
    if fore > cur:
        ans += fore - cur
    else:
        fore = cur

print(ans)