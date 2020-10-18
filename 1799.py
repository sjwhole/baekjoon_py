import sys


def possible(x, y):

def dfs(x, y, count):

    ans = max(ans, count)


n = int(sys.stdin.readline())
chess = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 1, -1], [1, 1, -1, -1]
visited = [[[0] * n] for _ in range(n)]
ans = [0, 0]

# 짝수는 0, 홀수는 1
dfs(0, 0, 0)
dfs(1, 1, 0)
print(sum(ans))
