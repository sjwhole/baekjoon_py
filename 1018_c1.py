import sys

row, column = map(int, sys.stdin.readline().split())
table = []
start_B = [[] for _ in range(row)]
start_W = [[] for _ in range(row)]
for _ in range(row):
    table.append(sys.stdin.readline())

# 시작이 B
for i in range(0, row, 2):
    for j in range(0, column, 2):
        if table[i][j] != "B":
            start_B[i].append(j)
        else:
            start_W[i].append(j)
for i in range(0, row, 2):
    for j in range(1, column, 2):
        if table[i][j] != "W":
            start_B[i].append(j)
        else:
            start_W[i].append(j)
for i in range(1, row, 2):
    for j in range(0, column, 2):
        if table[i][j] != "W":
            start_B[i].append(j)
        else:
            start_W[i].append(j)
for i in range(1, row, 2):
    for j in range(1, column, 2):
        if table[i][j] != "B":
            start_B[i].append(j)
        else:
            start_W[i].append(j)


def get_column_length(ls):
    min_info = []
    max_info = []
    for i in range(len(ls)):
        if len(ls[i]) != 0:
            min_info.append(min(ls[i]))
            max_info.append(max(ls[i]))
    column_length = max(max_info) - min(min_info)
    return column_length


def get_row_length(ls):
    for i in range(len(ls)):
        if len(ls[i]) != 0:
            start = i
            break
    for j in range(len(ls) - 1, -1, -1):
        if len(ls[j]) != 0:
            end = j
            break
    if start == end:
        return 1
    else:
        return end - start + 1



# B
cb = get_column_length(start_B)
rb = get_row_length(start_B)

if cb >= rb:
    length_b = cb
else:
    length_b = rb

# W

cw = get_column_length(start_W)
rw = get_row_length(start_W)

if cw >= rw:
    length_w = cw
else:
    length_w = rw

if length_b <= length_w:
    print(length_b)
else:
    print(length_w)
# for j in start_B:
#     print(j)
# print(cb)
# print(length_b, length_w)
