import sys
import io

_INPUT = """\
8
WRWWRWRR
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
c = input()
i = 0
j = n - 1

ans = 0
left = True
right = False
while i <= j:
    if left and c[i] == 'R':
        i += 1
    elif left and c[i] == 'W':
        i += 1
        left = False
        right = True
    elif right and c[j] == 'W':
        j -= 1
    elif right and c[j] == 'R':
        j -= 1
        left = True
        right = False
        ans += 1

print(ans)