import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, count):
    global ans
    ans = max(ans, count)

    for i in range(4):
        x_new = x + dx[i]
        y_new = y + dy[i]

        if 0 <= x_new < R and 0 <= y_new < C and not visited[table[x_new][y_new]]:
            visited[table[x_new][y_new]] = 1
            dfs(x_new, y_new, count + 1)
            visited[table[x_new][y_new]] = 0


R, C = map(int, sys.stdin.readline().split())
ans = 1
visited = [0] * 26
table = [list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(R)]
ans = 0
visited[table[0][0]] = 1
dfs(0, 0, 1)

print(ans)