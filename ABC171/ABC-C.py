import sys
import io

_INPUT = """\
706
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

l = 0
num = 0
while  n > num:
    l += 1
    num += 26 ** l

num = num // 26
mod = n - num

ans = []
while l > 0:
    q = mod // (26 ** (l - 1))
    mod %= (26 ** (l - 1))
    ans.append(q)
    l -= 1

res =''
for e in ans:
    res += chr(e + 97)

print(res)