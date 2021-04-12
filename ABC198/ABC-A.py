import sys
import io

_INPUT = """\
2
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

ans = n - 1
print(ans)