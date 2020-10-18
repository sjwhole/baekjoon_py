import sys
from math import log2


class Solve:
    def __init__(self):
        self.N, self.M = map(int, sys.stdin.readline().split())
        self.switch = [0] * self.N
        self.tree = [0] * (2 ** (int(log2(self.N)) + 2))
        self.lazy = [0] * (2 ** (int(log2(self.N)) + 2))

    def update_lazy(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[node * 2] = int(not(self.lazy[node * 2]))
                self.lazy[node * 2 + 1] = int(not(self.lazy[node * 2 + 1]))
            self.lazy[node] = 0

    def update_range(self, node, start, end, left, right):
        self.update_lazy(node, start, end)
        if right < start or end < left:
            return self.tree[node]
        if left <= start and end <= right:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[node * 2] = int(not(self.lazy[node * 2]))
                self.lazy[node * 2 + 1] = int(not(self.lazy[node * 2 + 1]))
            return self.tree[node]
        mid = (start + end) // 2
        self.update_range(node * 2, start, mid, left, right)
        self.update_range(node * 2 + 1, mid + 1, end, left, right)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def add(self, node, start, end, left, right):
        self.update_lazy(node, start, end)
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.add(node * 2, start, mid, left, right) + self.add(node * 2 + 1, mid + 1, end, left, right)

    def sol(self):
        for _ in range(self.M):
            temp_list = list(map(int, sys.stdin.readline().split()))
            if temp_list[0] == 0:
                self.update_range(1, 0, self.N - 1, temp_list[1] - 1, temp_list[2] - 1)
            else:
                print(self.add(1, 0, self.N - 1, temp_list[1] - 1, temp_list[2] - 1))


solve = Solve()
solve.sol()
