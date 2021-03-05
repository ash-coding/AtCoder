import sys
import io

_INPUT = """\
a
"""
sys.stdin = io.StringIO(_INPUT)

s = input()

n = len(s)
ans = 'Yes'
for i in range(n):
    t = s[i]
    if (i + 1) % 2 == 0:
        if t.islower():
            ans = 'No'
    else:
        if t.isupper():
            ans = 'No'

print(ans)