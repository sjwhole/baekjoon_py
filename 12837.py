import sys


class Solve:
    def __init__(self):
        self.N, self.Q = map(int, sys.stdin.readline().split())
        self.num_list = [0] * self.N
        self.tree = [0] * 3000000
        self.init(1, 0, self.N - 1)

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.num_list[start]
            return self.tree[node]
        else:
            self.tree[node] = self.init(node * 2, start, (start + end) // 2) + self.init(node * 2 + 1,
                                                                                         (start + end) // 2 + 1, end)
            return self.tree[node]

    def update(self, node, start, end, index, diff):
        if index < start or index > end:
            return

        self.tree[node] += diff

        if start != end:
            self.update(node * 2, start, (start + end) // 2, index, diff)
            self.update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

    def add(self, node, start, end, left, right):
        if left > end or right < start:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        return self.add(node * 2, start, (start + end) // 2, left, right) + self.add(node * 2 + 1,
                                                                                     (start + end) // 2 + 1, end,
                                                                                     left, right)

    def sol(self):
        for _ in range(self.Q):
            a, b, c = map(int, sys.stdin.readline().split())
            if a == 1:
                b -= 1
                diff = c - self.num_list[b]
                self.num_list[b] += c
                self.update(1, 0, self.N - 1, b, diff)
            else:
                print(self.add(1, 0, self.N - 1, b - 1, c - 1))


solve = Solve()
solve.sol()
