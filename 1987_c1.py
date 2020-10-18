import sys


def dfs(x, y, path, count):
    path += map_list[x][y]
    count += 1
    possible = []
    if x > 0:
        possible.append([x - 1, y])
    if x + 1 < R:
        possible.append([x + 1, y])
    if y > 0:
        possible.append([x, y - 1])
    if y + 1 < C:
        possible.append([x, y + 1])

    possible_copy = possible[:]
    for xy in possible:
        if map_list[xy[0]][xy[1]] in path:
            possible_copy.remove(xy)
    if possible_copy:
        for xy in possible_copy:
            dfs(xy[0], xy[1], path, count)
    else:
        count_list.append(count)


R, C = map(int, sys.stdin.readline().split())
map_list = []
count_list = []
for _ in range(R):
    map_list.append(sys.stdin.readline()[:-1])
dfs(0, 0, "", 0)
print(max(count_list))
