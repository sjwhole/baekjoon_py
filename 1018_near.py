import sys

row, column = map(int, sys.stdin.readline().split())
table = []
relation = []
row_data = []
column_data = []
for _ in range(row):
    table.append(sys.stdin.readline())
for i in range(row):
    for j in range(column - 1):
        if table[i][j] == table[i][j + 1]:
            row_data.append(i)
            column_data.append(j)
for k in range(column):
    for l in range(row - 1):
        if table[l][k] == table[l + 1][k]:
            row_data.append(l)
            column_data.append(k)

row_data = sorted(list(set(row_data)))
column_data = sorted(list(set(column_data)))
row_length = row_data[-1] - row_data[0]
column_length = column_data[-1] - column_data[0]
if row_length >= column_length:
    print(row_length)
else:
    print(column_length)

