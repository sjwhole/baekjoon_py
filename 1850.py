import sys
from math import gcd

a, b = map(int, sys.stdin.readline().split())
print("1" * gcd(a, b))