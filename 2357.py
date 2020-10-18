import sys


class Solve:
    def __init__(self):
        self.N, self.M = map(int, sys.stdin.readline().split())
        self.num_list = [0] * self.N
        for i in range(self.N):
            self.num_list[i] = int(sys.stdin.readline())
        self.min_tree = [0] * 3000000
        self.max_tree = [0] * 3000000
        self.min_init(1, 0, self.N - 1)
        self.max_init(1, 0, self.N - 1)

    def min_init(self, node, start, end):
        if start == end:
            self.min_tree[node] = self.num_list[start]
            return self.min_tree[node]
        else:
            self.min_tree[node] = min(self.min_init(node * 2, start, (start + end) // 2),
                                      self.min_init(node * 2 + 1, (start + end) // 2 + 1, end))
            return self.min_tree[node]

    def max_init(self, node, start, end):
        if start == end:
            self.max_tree[node] = self.num_list[start]
            return self.max_tree[node]
        else:
            self.max_tree[node] = max(self.max_init(node * 2, start, (start + end) // 2),
                                      self.max_init(node * 2 + 1, (start + end) // 2 + 1, end))
            return self.max_tree[node]

    def get_min(self, node, start, end, left, right):
        if left > end or right < start:
            return 1000000001
        if left <= start and end <= right:
            return self.min_tree[node]

        return min(self.get_min(node * 2, start, (start + end) // 2, left, right), self.get_min(node * 2 + 1,
                                                                                                (start + end) // 2 + 1,
                                                                                                end,
                                                                                                left, right))

    def get_max(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.max_tree[node]

        return max(self.get_max(node * 2, start, (start + end) // 2, left, right), self.get_max(node * 2 + 1,
                                                                                                (start + end) // 2 + 1,
                                                                                                end,
                                                                                                left, right))

    def sol(self):
        for _ in range(self.M):
            a, b = map(int, sys.stdin.readline().split())
            print(self.get_min(1, 0, self.N - 1, a - 1, b - 1), self.get_max(1, 0, self.N - 1, a - 1, b - 1))


solve = Solve()
solve.sol()
