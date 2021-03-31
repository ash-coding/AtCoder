import sys
import io

_INPUT = """\
SSS
"""
sys.stdin = io.StringIO(_INPUT)

s = input()

if s == 'RRR':
    ans = 3
elif s == 'SSS':
    ans = 0
elif s == 'RSS' or s == 'SRS' or s == 'SSR' or s == 'RSR':
    ans = 1
else:
    ans = 2

print(ans)