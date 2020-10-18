import sys


class Solve:
    def __init__(self):
        self.N, self.M = map(int, sys.stdin.readline().split())
        self.in_list = [0] * self.M + [1] * self.N
        self.index_list = list(range(self.M, self.M + self.N))
        self.tree = [0] * 3000000
        self.init(1, 0, self.N + self.M - 1)

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.in_list[start]
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
        dvd_list = list(map(int, sys.stdin.readline().split()))
        for i in range(self.M):
            dvd = dvd_list[i]
            dvd -= 1
            now = self.index_list[dvd]
            print(self.add(1, 0, self.N + self.M - 1, 0, now - 1), end=" ")
            move = self.M - i - 1
            self.in_list[now] = 0
            self.in_list[move] = 1
            self.index_list[dvd] = move
            self.update(1, 0, self.N + self.M - 1, now, -1)
            self.update(1, 0, self.N + self.M - 1, move, 1)


for _ in range(int(sys.stdin.readline())):
    solve = Solve()
    solve.sol()
    print()
