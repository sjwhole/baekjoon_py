import sys

row, column = map(int, sys.stdin.readline().split())
table = []
data_row = []
data_column = []
for _ in range(row):
    table.append(sys.stdin.readline())
for i in range(row):
    data_temp =[]
    for j in range(column - 1):
        if table[i][j] == table[i][j + 1]:
            data_temp.append(0)
        else:
            data_temp.append(1)
    data_row.append(data_temp)
for k in range(column):
    data_temp =[]
    for l in range(row - 1):
        if table[l][k] == table[l + 1][k]:
            data_temp.append(0)
        else:
            data_temp.append(1)
    data_column.append(data_temp)
for row_rel in data_row:
    print(row_rel)
print()
for column_rel in data_column:
    print(column_rel)
