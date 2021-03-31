import sys
import io

_INPUT = """\
6
4 5 4 3 3 5
"""
sys.stdin = io.StringIO(_INPUT)

import itertools
n = int(input())
L = list(map(int, input().split()))

ans = 0
for Li, Lj, Lk in itertools.combinations(L, 3):
    if Li != Lj and Li != Lk and Lj != Lk:
        lst = [Li, Lj, Lk]
        lst.sort(reverse = True)
        if lst[0] < lst[1] + lst[2]:
            ans += 1

print(ans)