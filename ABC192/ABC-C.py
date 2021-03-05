import sys
import io

_INPUT = """\
6174 100000
"""
sys.stdin = io.StringIO(_INPUT)

n, k = map(int, input().split())

def f(x):
    g1 = int(''.join(sorted(str(x))))
    g2 = int(''.join(sorted(str(x), reverse = True)))
    return g2 - g1

for i in range(k):
    ans = f(n)
    n = ans

print(n)
