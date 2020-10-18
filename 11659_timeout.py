import sys


N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum(num[i - 1: j]))