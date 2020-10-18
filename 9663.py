import sys


def dfs(row, num):
    global count
    if len(row) == num:
        count += 1
        return
    possible = [i for i in range(N)]
    for idx, place in enumerate(row):
        if place in possible:
            possible.remove(place)
        d = len(row) - idx
        if place + d in possible:
            possible.remove(place + d)
        if place - d in possible:
            possible.remove(place - d)
    if len(possible) != 0:
        for add_place in possible:
            row_cp = row[:]
            row_cp.append(add_place)
            dfs(row_cp, num)
    else:
        return


N = int(sys.stdin.readline())
count = 0
for i in range(N):
    dfs([i], N)
print(count)
