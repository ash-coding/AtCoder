import sys
import io

_INPUT = """\
3
1 5 7
"""
sys.stdin = io.StringIO(_INPUT)

import itertools
n = int(input())
A = list(map(int, input().split()))

ans = 0
for x in A:
    ans ^= x

for i in range(1, n):
    for x in itertools.combinations(range(1, n), i):
        temp = []
        c = 0
        for j, a in enumerate(A):
            if j in x:
                temp.append(c)
                c = a
            else:
                c |= a
            if j == n - 1:
                temp.append(c)
        c = 0
        for y in temp:
            c ^= y
        ans = min(ans, c)
print(ans)

