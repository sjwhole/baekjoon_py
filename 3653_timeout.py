import sys

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    order = list(range(n, 0, -1))
    for movie in list(map(int, sys.stdin.readline().split())):
        print(n - order.index(movie) - 1, end=" ")
        order.remove(movie)
        order.append(movie)
    print()
