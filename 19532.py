import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
solved = False
for x in range(-999, 1000):
    if solved:
        break
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(f"{x} {y}")
            solved = True
            break
