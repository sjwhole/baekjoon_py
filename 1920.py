import sys


sys.stdin.readline()
num_list = list(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
for num in list(map(int, sys.stdin.readline().split())):
    if num in num_list:
        print("1")
    else:
        print("0")