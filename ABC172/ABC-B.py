import sys
import io

_INPUT = """\
cupofcoffee
cupofhottea
"""
sys.stdin = io.StringIO(_INPUT)

s = input()
t = input()

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1

print(ans)