import sys
import io

_INPUT = """\
1210
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
s = str(n)
s = s.strip('0')

m = len(s) // 2
ans = 'Yes'
for i in range(m):
    if s[i] != s[-i-1]:
        ans = 'No'
        break

print(ans)