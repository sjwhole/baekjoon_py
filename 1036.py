import sys


NOTATION ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

info_list = [[] for _ in range(51)]
T = int(sys.stdin.readline())
for i in range(T):
    num = sys.stdin.readline()
    for j in range(1, len(num)):
        info_list[j - 1].append(num[-(j + 1)])
print(info_list)