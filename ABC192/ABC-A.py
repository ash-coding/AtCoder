import sys
import io

_INPUT = """\
1000
"""
sys.stdin = io.StringIO(_INPUT)

x = int(input())

ans = 100 - x % 100
print(ans)