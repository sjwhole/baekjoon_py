import sys


def back_tracking(n):
    if n == M:
        for i in range(M):
            print(num_list[i], end=" ")
        print()
        return
    for i in range(N):
        if visited[i] == 0:
            num_list[n] = i + 1
            visited[i] = 1
            back_tracking(n + 1)
            visited[i] = 0


N, M = map(int, sys.stdin.readline().split())
visited = [0] * N
num_list = [0] * N
back_tracking(0)
