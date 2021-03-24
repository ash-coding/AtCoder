import sys
import io

_INPUT = """\
4
1 1 1 1
3
1 2
2 1
3 5
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a = list(map(int, input().split()))
q = int(input())

acount = [0] * (100001)
for x in a:
    acount[x] += 1

ans = sum(a)
for _ in range(q):
    b, c = map(int, input().split())
    if acount[b] != 0:
        ans += (c - b) * acount[b]
        acount[c] += acount[b]
        acount[b] = 0
    print(ans)