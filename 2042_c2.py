import sys


class Solve:
    def __init__(self, node, start, end):
        self.tree = [0] * 3000000
        self.init(node, start, end)

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = num_list[start]
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


N, M, K = map(int, sys.stdin.readline().split())
num_list = [0] * N
for i in range(N):
    num_list[i] = int(sys.stdin.readline())
solve = Solve(1, 0, N - 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        b -= 1
        diff = c - num_list[b]
        num_list[b] = c
        solve.update(1, 0, N - 1, b, diff)
    else:
        print(solve.add(1, 0, N - 1, b - 1, c - 1))
