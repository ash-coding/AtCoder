import sys
import io

_INPUT = """\
4
WRWW
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
c = input()
i = 0
j = n - 1

ans = 0
l = True
while i <= j:
    if l:
        if c[i] == 'W':
            l = False
        i += 1
    else:
        if c[j] == 'R':
            l = True
            ans += 1
        j -= 1

print(ans)