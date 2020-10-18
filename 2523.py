import sys

num = int(sys.stdin.readline())
for i in range(1, num):
    print("*" * i)
for j in range(num, 0, -1):
    print("*" * j)