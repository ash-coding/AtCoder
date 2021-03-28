import sys
import io

_INPUT = """\
6
5 3
7 4
"""
sys.stdin = io.StringIO(_INPUT)

import math
n = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

theta = 360 / n * math.pi / 180
rx = (x0 + xn2) / 2
ry = (y0 + yn2) / 2

x0 -= rx
y0 -= ry

x1 = x0 * math.cos(theta) - y0 * math.sin(theta) + rx
y1 = x0 * math.sin(theta) + y0 * math.cos(theta) + ry

print(x1, y1)