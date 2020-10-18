import sys


N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
sum_list = [num[0]] + [0] * (N - 1)
for i in range(1, N):
    sum_list[i] = sum_list[i - 1] + num[i]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sum_list[j - 1])
    else:
        print(sum_list[j - 1] - sum_list[i - 2])
