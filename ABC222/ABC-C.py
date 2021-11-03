import sys
import io

_INPUT = """\
2 3
GCP
PPP
CCC
PPC
"""
sys.stdin = io.StringIO(_INPUT)

n, m = map(int, input().split())
A = [[''] * (2*n) for _ in range(m)]

for i in range(2*n):
    s = input()
    for j, t in enumerate(s):
        A[j][i] = t

rank = [[0, i] for i in range(2*n)]

def janken(s1, s2):
    if s1 == s2:
        res = -1
    elif (s1 == 'G' and s2 == 'C') or (s1 == 'P' and s2 == 'G') or (s1 == 'C' and s2 == 'P'):
        res = 0
    else:
        res = 1
    return res

for g in range(m):
    for i in range(n):
        p1 = rank[2*i][1]
        p2 = rank[2*i+1][1]
        s1 = A[g][p1]
        s2 = A[g][p2]
        res = janken(s1, s2)
        if res != -1:
            rank[2*i+res][0] -= 1
    rank.sort()

for r in rank:
    print(r[1] + 1)