import sys
import io

_INPUT = """\
1900
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
if n % 1000 == 0:
    ans = 0
else:
    ans = 1000 - n % 1000
print(ans)