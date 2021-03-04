import sys
import io

_INPUT = """\
10000000000
"""
sys.stdin = io.StringIO(_INPUT)

import math
n = int(input())

limit = math.floor(math.sqrt(n))
data = {0}
for i in range(2, limit + 1):
    num = i * i
    while num <= n:
        data.add(num)
        num *= i

print(n - len(data) + 1)
