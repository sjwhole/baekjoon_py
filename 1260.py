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
    front, rear = 0, 0
    queue = []
    bfs_visit[start] = 1
    rear += 1
    queue.append(start)
    print(start, end=" ")
    while front < rear:
        now = queue[front]
        front += 1
        for i in range(1, num + 1):
            if graph[now][i] == 1 and bfs_visit[i] == 0:
                bfs_visit[i] = 1
                queue.append(i)
                rear += 1
                print(i, end=" ")
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