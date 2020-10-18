import sys


def factorial(x):
    num = 1
    for i in range(2, x + 1):
        num *= i
    return num


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


T = int(sys.stdin.readline())
for _ in range(T):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(combination(n2, n1))