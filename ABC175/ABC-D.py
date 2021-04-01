import sys
import io

_INPUT = """\
5 2
2 4 5 1 3
3 4 -10 -8 8

"""
sys.stdin = io.StringIO(_INPUT)

n, k = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))
c = list(map(int, input().split()))

ans = max(c)
for i in range(n):
    pos = i
    score = 0
    scores = [0]
    while p[pos] != i:
        pos = p[pos]
        score += c[pos]
        scores.append(score)
    score_total = scores[-1] + c[i]
    score_len = len(scores)

    for j in range(score_len):
        if j <= k and j != 0:
            cycles = (k - j) // score_len
            e = scores[j] + max(0, score_total) * cycles
            ans = max(ans, e)
        elif j == 0 and k >= score_len:
            e = score_total * k // score_len
            ans = max(ans, e)

print(ans)

