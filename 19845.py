import sys

n, count = map(int, sys.stdin.readline().split())
info = list(map(int, sys.stdin.readline().split()))

for _ in range(count):
    x, y = map(int, sys.stdin.readline().split())
    row_erase = info[y - 1] - x + 1
    if info[-1] >= x:
        sys.stdout.write(str(row_erase + n - y) + '\n')
        continue
    column_erase = 0
    for i in range(y, n):
        if info[i] < x:
            column_erase = i - y
            break
    sys.stdout.write(str(row_erase + column_erase) + '\n')