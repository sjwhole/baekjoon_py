import sys


def get_list():
    ls = list(map(int, sys.stdin.readline().split()))
    return ls


length = int(sys.stdin.readline())

A = get_list()
B = get_list()

A.sort()
B.sort()

hab = 0
for i in range(length):
    hab += A[i] * B[-i - 1]
print(hab)