import sys
import io

_INPUT = """\
hellospaceRhellospace
"""
sys.stdin = io.StringIO(_INPUT)

s = input()
t = ''
n = len(s)

flag = False
key = ''
for i in range(n):
    if s[i] == 'R':
        if flag:
            if t != '':
                key = t[-1]
            else:
                key = ''
        else:
            if t != '':
                key = t[0]
            else:
                key = ''
        flag = not flag
    elif s[i] == key:
        if flag:
            t = t[1:]
            if t != '':
                key = t[0]
            else:
                key = ''
        else:
            t = t[:-1]
            if t != '':
                key = t[-1]
            else:
                key = ''
    else:
        key = s[i]
        if flag:
            t = s[i] + t           
        else:
            t = t + s[i]

if flag:
    t = t[::-1]

print(t)