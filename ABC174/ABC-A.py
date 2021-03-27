import sys
import io

_INPUT = """\
30
"""
sys.stdin = io.StringIO(_INPUT)

x = int(input())
if x >= 30:
    print('Yes')
else:
    print('No')