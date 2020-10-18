import sys
from math import log2


class Solve:
    def __init__(self):
        self.N, self.M, self.K = map(int, sys.stdin.readline().split())
        self.num_list = [int(sys.stdin.readline()) for _ in range(self.N)]
        idx = 2 ** (int(log2(self.N)) + 2)
        self.tree = [0] * idx
        self.lazy = [0] * idx
        self.init(1, 0, self.N - 1)

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.num_list[start]
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = self.init(node * 2, start, mid) + self.init(node * 2 + 1, mid + 1, end)
        return self.tree[node]

    def update_lazy(self, node, start, end):
        if self.lazy[node]:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update_range(self, node, start, end, left, right, diff):
        self.update_lazy(node, start, end)
        if right < start or end < left:
            return
        if left <= start and end <= right:
            self.tree[node] += (end - start + 1) * diff
            if start != end:
                self.lazy[node * 2] += diff
                self.lazy[node * 2 + 1] += diff
            return
        mid = (start + end) // 2
        self.update_range(node * 2, start, mid, left, right, diff)
        self.update_range(node * 2 + 1, mid + 1, end, left, right, diff)
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
        for _ in range(self.M + self.K):
            temp_list = list(map(int, sys.stdin.readline().split()))
            if temp_list[0] == 1:
                self.update_range(1, 0, self.N - 1, temp_list[1] - 1, temp_list[2] - 1, temp_list[3])
            else:
                print(self.add(1, 0, self.N - 1, temp_list[1] - 1, temp_list[2] - 1))


solve = Solve()
solve.sol()
