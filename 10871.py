import sys

length, less = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
for num in num_list:
    if num < less:
        print(num, end=" ")