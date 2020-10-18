import sys


def compare(x, y):
    if a < b:
        return "<"
    if a > b:
        return ">"
    if a == b:
        return "=="


a, b = map(int, sys.stdin.readline().split())
print(compare(a, b))
