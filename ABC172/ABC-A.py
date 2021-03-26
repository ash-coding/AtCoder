import sys
import io

_INPUT = """\
2
"""
sys.stdin = io.StringIO(_INPUT)

a = int(input())

print(a + a ** 2 + a ** 3)