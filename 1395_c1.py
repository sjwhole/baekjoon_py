import sys
from math import log2, pow


class Solve:
    def __init__(self):
        self.N, self.M = map(int, sys.stdin.readline().split())
        self.tree = [0] * pow(2, int(log2(self.N) + 2))
        self.lazy = [0] * pow(2, int(log2(self.N) + 2))

    def update_lazy(self, node, start, end, left, right):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0
