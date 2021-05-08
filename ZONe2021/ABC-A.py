import sys
import io

_INPUT = """\
helloAtZoner
"""
sys.stdin = io.StringIO(_INPUT)

s = input()

ans = s.count('ZONe')
print(ans)