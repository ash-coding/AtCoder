import sys
import io

_INPUT = """\
send
more
money
"""
sys.stdin = io.StringIO(_INPUT)

import itertools
s1 = input()
s2 = input()
s3 = input()

ss_set = set(s1 + s2 + s3)
s_set = list(ss_set)
s1_index = [s_set.index(s) for s in s1]
s2_index = [s_set.index(s) for s in s2]
s3_index = [s_set.index(s) for s in s3]

if len(s_set) > 10:
    ans = 'UNSOLVABLE'
else:
    ans = 'UNSOLVABLE'
    for x in itertools.permutations(range(10), len(s_set)):
        if x[s1_index[0]] == 0 or x[s2_index[0]] == 0 or x[s3_index[0]] == 0:
            continue
        s1_int = 0
        for i in s1_index:
            s1_int *= 10
            s1_int += x[i]
        s2_int = 0
        for i in s2_index:
            s2_int *= 10
            s2_int += x[i]
        s3_int = 0
        for i in s3_index:
            s3_int *= 10
            s3_int += x[i]
        if s1_int + s2_int == s3_int:
            ans = [s1_int, s2_int, s3_int]
            break
if ans == 'UNSOLVABLE':
    print(ans)
else:
    for i in ans:
        print(i)