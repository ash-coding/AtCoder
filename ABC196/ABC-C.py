import sys
import io

_INPUT = """\
10000000
"""
sys.stdin = io.StringIO(_INPUT)

import itertools
n = input()

digit = len(n) // 2
ans = 0
for i in range(digit):
    for num in itertools.product(range(10), repeat = i + 1):
        if num[0] == 0:
            continue
        else:
            t = ''
            for a in num:
                t += str(a)
            t += t
            if int(t) <= int(n):
                ans += 1

print(ans)