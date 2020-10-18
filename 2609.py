import sys


def isbigger(x, y):
    if x < y:
        return y, x
    else:
        return x, y


def gcd(x, y):
    x, y = isbigger(x, y)
    while x % y != 0:
        x, y = y, x % y
    return y


def lcm(x, y):
    x, y = isbigger(x, y)
    return x * y // gcd(x, y)


a, b = map(int, sys.stdin.readline().split())
print(gcd(a, b))
print(lcm(b, a))
