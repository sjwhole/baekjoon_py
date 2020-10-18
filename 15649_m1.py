import sys


def dfs(n, m):
    if len(table) == m:
        for num in table:
            print(num, end=" ")
        return

    for i in range(n):
        table.append(nums[i])
        if not visited[nums[i] - 1]:
            visited[nums[i]] = 1
            dfs(n, m)
            visited[nums[i]] = 0


N, M = map(int, sys.stdin.readline().split())
table = []
visited = [0] * N
dfs(N, M)
