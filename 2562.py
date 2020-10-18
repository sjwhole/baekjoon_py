import sys


num = []
for _ in range(9):
    num.append(int(sys.stdin.readline()))
print(max(num))
print(num.index(max(num)) + 1)