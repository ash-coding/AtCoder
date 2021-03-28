import sys
import io

_INPUT = """\
aab
"""
sys.stdin = io.StringIO(_INPUT)

s = input()
ans = s[1] + s[2] + s[0]
print(ans)