import sys


class Solve:
    def __init__(self):
        self.N, self.M, self.K = map(int, sys.stdin.readline().split())
        self.num_list = [0] * self.N
        for i in range(self.N):
            self.num_list[i] = int(sys.stdin.readline())
        self.tree = [0] * 3000000
        self.init(1, 0, self.N - 1)

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.num_list[start]
            return self.tree[node]
        else:
            self.tree[node] = self.init(node * 2, start, (start + end) // 2) * self.init(node * 2 + 1,
                                                                                         (start + end) // 2 + 1, end) % 1000000007
            return self.tree[node]

    def update(self, node, start, end, index, diff):
        if index < start or index > end:
            return

        self.tree[node] *= diff

        if start != end:
            self.update(node * 2, start, (start + end) // 2, index, diff)
            self.update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

    def mul(self, node, start, end, left, right):
        if left > end or right < start:
            return 1

        if left <= start and end <= right:
            return self.tree[node]

        return self.mul(node * 2, start, (start + end) // 2, left, right) * self.mul(node * 2 + 1,
                                                                                     (start + end) // 2 + 1, end,
                                                                                     left, right)

    def sol(self):
        for _ in range(self.M + self.K):
            a, b, c = map(int, sys.stdin.readline().split())
            if a == 1:
                b -= 1
                prev = self.num_list[b]
                if prev == 0 and c == 0:
                    continue
                if c == 0:
                    diff = 1 / prev
                    self.update(1, 0, self.N - 1, b, diff)
                    self.num_list[b] = 0
                    continue
                if prev == 0:
                    diff = c
                else:
                    diff = c / self.num_list[b]
                self.num_list[b] = c
                self.update(1, 0, self.N - 1, b, diff)
            else:
                if 0 in self.num_list[b - 1: c]:
                    print(0)
                    continue
                print(int(self.mul(1, 0, self.N - 1, b - 1, c - 1) % 1000000007))


solve = Solve()
solve.sol()
