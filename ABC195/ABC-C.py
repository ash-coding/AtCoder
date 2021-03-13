import sys
import io

_INPUT = """\
1000000
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

i = 0
m = n // 1000
ans = 0
while m >= 1000:
    i += 1
    t = '9' * 3 + '0' * i * 3
    ans += int(t) * i
    m //= 1000

if n > 999:
    ans += (n - (1000 ** (i + 1)) + 1) * (i + 1)

print(ans)