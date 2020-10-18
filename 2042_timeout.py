import sys


N, M, K = map(int, sys.stdin.readline().split())
num_list = [0] * N
# sum_list = [num_list[0]] + [0] * (N - 1)
for i in range(N):
    num_list[i] = int(sys.stdin.readline())
# for j in range(N):
#     sum_list[j] = sum_list[j - 1] + num_list[j]
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        num_list[b - 1] = c
    else:
        print(sum(num_list[b - 1: c]))