import sys


table = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            table[i][j] = 1
s = 0
for row in table:
    s += row.count(1)
print(s)