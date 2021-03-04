import sys
import io

_INPUT = """\
100000
3226#
3597#
"""
sys.stdin = io.StringIO(_INPUT)

k = int(input())
s = input()
t = input()

all_cards = [k] * 10

sc = [0] * 10
for i in s[:4]:
    sc[int(i)] += 1
    all_cards[int(i)] -= 1

tc = [0] * 10
for i in t[:4]:
    tc[int(i)] += 1
    all_cards[int(i)] -= 1

swin = 0
all_cards[0] = 0
for scard in range(1, 10):
    for tcard in range(1, 10):
        if scard == tcard and all_cards[scard] - 2 < 0:
            continue
        elif all_cards[scard] - 1 < 0 or all_cards[tcard] - 1 < 0:
            continue
        sp = 0
        tp = 0
        for i, ci in enumerate(sc):
            if scard == i:
                ci += 1
            sp += i * (10 ** ci)
        for i, ci in enumerate(tc):
            if tcard == i:
                ci += 1
            tp += i * (10 ** ci)
        if scard == tcard:
            s1 = all_cards[scard]
            s2 = s1 - 1
        else:
            s1 = all_cards[scard]
            s2 = all_cards[tcard]
        if sp > tp:
            swin += s1 * s2

all_cases = sum(all_cards) * (sum(all_cards) - 1)
ans = swin / all_cases
print(ans)