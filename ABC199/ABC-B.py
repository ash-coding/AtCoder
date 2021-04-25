import sys
import io

_INPUT = """\
3
3 2 5
6 9 8
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

amax = max(a)
bmin = min(b)

ans = bmin - amax + 1
ans = max(0, ans)
print(ans)