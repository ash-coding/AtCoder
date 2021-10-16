import sys
import io

_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)

n = input()
ans = '0' * (4 - len(n)) + n

print(ans)