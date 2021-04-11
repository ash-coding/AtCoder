import sys
import io

_INPUT = """\
31415926535897932384626433832795028841971693993751058209749445923078164062862089986280
"""
sys.stdin = io.StringIO(_INPUT)

n = input()
s = 0
for i in n:
    s += int(i)

if s % 9 == 0:
    print('Yes')
else:
    print('No')