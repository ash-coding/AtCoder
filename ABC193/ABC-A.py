import sys
import io

_INPUT = """\
7 6
"""
sys.stdin = io.StringIO(_INPUT)

a, b = map(int, input().split())

ans = (a - b) / a * 100
print(ans)