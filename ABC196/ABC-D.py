import sys
import io

_INPUT = """\
4 4 8 0
"""
sys.stdin = io.StringIO(_INPUT)

h, w, a, b = map(int, input().split())

ans = 0
def dfs(i, bit, a, b):
    # i -> current grid
    # bit -> grid condition
    # a, b -> remaining number of tatami

    # Exit condition
    if i == h * w:
        global ans
        ans += 1
        return
    # Skip
    if bit >> i & 1:
        dfs(i + 1, bit, a, b)
        # return
    # set 1x1 tatami
    if b:
        dfs(i + 1, bit | 1 << i, a, b - 1)
    # set 2x1 tatami
    if a:
        # Horizontal
        if i % w != w - 1 and not bit & 1 << (i + 1):
            dfs(i + 1, bit | 1 << i | 1 << (i + 1), a - 1, b)
        # Vertical
        if i + w < h * w:
            dfs(i + 1, bit | 1 << i | 1 << (i + w), a - 1, b)

dfs(0, 0, a, b)
print(ans)
