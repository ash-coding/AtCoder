import sys
import io

_INPUT = """\
2
FLIP
2
2 0 0
1 1 4
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
s = list(input())
q = int(input())

flag = False
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        a -= 1
        b -= 1
        if flag:
            a = a + n if a < n else a - n
            b = b + n if b < n else b - n
        s[a], s[b] = s[b], s[a]
    else:
        flag = not flag

if flag:
    s[:n], s[n:] = s[n:], s[:n]

ans = ''.join(s)

print(ans)