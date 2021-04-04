import sys
import io

_INPUT = """\
8 9
0 1 2
0 3 2
1 1 3
1 1 4
0 2 4
1 4 1
0 4 2
0 0 0
1 0 0
"""
sys.stdin = io.StringIO(_INPUT)

sys.setrecursionlimit(1000000)
n, q = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
    
    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        self.par[rx] = ry
    
    def same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry

union_find_tree = UnionFind(n)
for _ in range(q):
    p, a, b = map(int, input().split())
    if p == 0:
        union_find_tree.unite(a, b)
    else:
        if union_find_tree.same(a, b):
            print('Yes')
        else:
            print('No')