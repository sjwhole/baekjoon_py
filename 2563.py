import sys


table = [[0] * 100 for _ in range(100)]
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            table[i][j] = 1
s = 0
for row in table:
    s += row.count(1)
print(s)