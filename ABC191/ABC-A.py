import sys
import io

_INPUT = """\
10 3 5 20
"""
sys.stdin = io.StringIO(_INPUT)

v, t, s, d = map(int, input().split())

start = v * t
end = v * s
ans = 'No'
if d < start or end < d:
    ans = 'Yes'

print(ans)