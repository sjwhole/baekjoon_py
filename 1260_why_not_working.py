import sys

graph = [[0] * 1001 for _ in range(1001)]
dfs_visit = [0] * 1001
bfs_visit = [0] * 1001


def dfs(start, num):
    dfs_visit[start] = 1
    print(start, end= " ")

    for i in range(1, num + 1):
        if graph[start][i] == 1 and dfs_visit[i] == 0:
            dfs(i, num)


def bfs(start, num):
    queue = []
    bfs_visit[start] = 1
    queue.append(start)
    print(start, end=" ")
    for i in range(num - 1):
        now = queue[i]
        for j in range(1, num + 1):
            if graph[now][j] == 1 and bfs_visit[j] == 0:
                bfs_visit[j] = 1
                queue.append(j)
                print(j, end=" ")
        if len(queue) == num:
            break


n, m, v = map(int, sys.stdin.readline().split())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
dfs(v, n)
print()
bfs(v, n)