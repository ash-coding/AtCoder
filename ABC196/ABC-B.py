import sys
import io

_INPUT = """\
84939825309432908832902189.9092309409809091329
"""
sys.stdin = io.StringIO(_INPUT)

x = input()
ans = ''

for t in x:
    if t == '.':
        break
    ans += t

print(int(ans))