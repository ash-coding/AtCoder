import sys
import io

_INPUT = """\
9
5 5
-4 4
4 3
6 3
-5 5
-3 2
2 2
3 3
1 4
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

# cx :list [c, x]
cx = []
for _ in range(n):
    x, c = list(map(int, input().split()))
    cx.append([c, x])

# sort ascending order by c
cx.sort()

# cur: current c, xmin: minimum x value, xmax: maximum x value
cur = cx[0][0]
xmin = cx[0][1]
xmax = cx[0][1]

# lst: list [cur, xmin, xmax]
lst = []
for c, x in cx:
    if c == cur:
        if x > xmax:
            xmax = x
    else:
        lst.append([cur, xmin, xmax])
        cur = c
        xmin = x
        xmax = x
lst.append([cur, xmin, xmax])

dp = [[0, 0] for _ in range(len(lst))]
if lst[0][1] * lst[0][2] < 0:
    dp[0][0] = 2 * abs(lst[0][2]) + abs(lst[0][1])
    dp[0][1] = 2 * abs(lst[0][1]) + abs(lst[0][2])
else:
    dp[0][0] = abs(lst[0][1])
    dp[0][1] = abs(lst[0][2])
left = lst[0][1]
right = lst[0][2]
for i in range(1, len(lst)):
    # left -> left
    if left > lst[i][2]:
        l1 = left - lst[i][1]
    else:
        l1 = (lst[i][2] - left) + (lst[i][2] - lst[i][1])

    # right -> left
    if right > lst[i][2]:
        l2 = right - lst[i][1]
    else:
        l2 = (lst[i][2] - right) + (lst[i][2] - lst[i][1])

    # left -> right
    if left < lst[i][1]:
        r1 = lst[i][2] - left
    else:
        r1 = (left - lst[i][1]) + (lst[i][2] - lst[i][1])
    
    # right -> right
    if right < lst[i][1]:
        r2 = lst[i][2] - right
    else:
        r2 = (right - lst[i][1]) + (lst[i][2] - lst[i][1])

    dp[i][0] = min(dp[i - 1][0] + l1, dp[i - 1][1] + l2)
    dp[i][1] = min(dp[i - 1][0] + r1, dp[i - 1][1] + r2)

    left = lst[i][1]
    right = lst[i][2]

ansl = dp[-1][0] + abs(left)
ansr = dp[-1][1] + abs(right)
ans = min(ansl, ansr)
print(ans)