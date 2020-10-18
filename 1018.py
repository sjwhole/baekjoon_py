import sys

row, column = map(int, sys.stdin.readline().split())
table = []
for _ in range(row):
    table.append(sys.stdin.readline())

count = []
for r in range(row - 7):
    for c in range(column - 7):
        cnt1 = 0
        cnt2 = 0
        for i in range(r, r + 8):
            for j in range(c, c + 8):
                if (i + j) % 2 == 0:
                    if table[i][j] != "B":
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if table[i][j] != "W":
                        cnt1 += 1
                    else:
                        cnt2 += 1
        count.append(cnt1)
        count.append(cnt2)

print(min(count))