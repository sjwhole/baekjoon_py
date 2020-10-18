import sys


def sum(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return sum(n - 1) + sum(n - 2) + sum(n - 3)


for _ in range(int(sys.stdin.readline())):
    print(sum(int(sys.stdin.readline())))
