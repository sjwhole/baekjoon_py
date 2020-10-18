import sys

def get_break_even_point(x, y, z):
    if b >= c:
        return -1
    point = a // (c -b)
    return point + 1


a, b, c = map(int, sys.stdin.readline().split())
print(get_break_even_point(a, b, c))