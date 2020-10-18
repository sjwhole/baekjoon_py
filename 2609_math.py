import math
import sys


x, y = map(int, sys.stdin.readline().split())
print(math.gcd(x, y))
print(x * y // math.gcd(x, y))