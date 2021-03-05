import sys
import io

_INPUT = """\
3 3
3 3 3
"""
sys.stdin = io.StringIO(_INPUT)

n, x = map(int, input().split())
a = list(map(int, input().split()))

a_dash = []
for i in range(n):
    if a[i] != x:
        a_dash.append(a[i])

print(*a_dash)