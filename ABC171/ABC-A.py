import sys
import io

_INPUT = """\
a
"""
sys.stdin = io.StringIO(_INPUT)

a = input()

if a.isupper():
    print('A')
else:
    print('a')