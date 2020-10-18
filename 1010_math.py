import sys
from math import factorial

T = int(sys.stdin.readline())
for _ in range(T):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(factorial(n2) // (factorial(n1) * factorial(n2 - n1)))