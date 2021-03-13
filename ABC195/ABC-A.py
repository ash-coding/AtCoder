import sys
import io

_INPUT = """\
10 125
"""
sys.stdin = io.StringIO(_INPUT)

m, h = map(int, input().split())

if h % m == 0:
    print('Yes')
else:
    print('No')