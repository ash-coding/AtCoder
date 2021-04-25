import sys
import io

_INPUT = """\
3 4 5
"""
sys.stdin = io.StringIO(_INPUT)

a, b, c = map(int, input().split())

if (a**2 + b**2) < c**2:
    print('Yes')
else:
    print('No')