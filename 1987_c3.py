import sys


def dfs(i, j, m):
    global ans

    ans = max(ans, m)

    for t in range(4):
        x, y = i + dx[t], j + dy[t]
        if 0 <= x < r and 0 <= y < c and not alpha[ord(table[x][y]) - 65]:
            alpha[ord(table[x][y]) - 65] = 1
            dfs(x, y, m + 1)
            alpha[ord(table[x][y]) - 65] = 0


r, c = map(int, sys.stdin.readline().split())
table = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
alpha = [0] * 26  # ASCII A=65 ~ Z=90
alpha[ord(table[0][0]) - 65] = 1
ans = 1

dfs(0, 0, 1)
print(ans)
