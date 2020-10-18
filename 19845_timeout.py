import sys

n, count = map(int, sys.stdin.readline().split())
info = list(map(int, sys.stdin.readline().split()))

for _ in range(count):
    x, y = map(int, sys.stdin.readline().split())
    row_erase = info[y - 1] - x + 1
    column_erase = 0
    for column in info[y:]:
        if column >= x:
            column_erase += 1
        else:
            break
    print(row_erase + column_erase)