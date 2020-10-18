import sys

num = sys.stdin.readline()

a, b = 0, 1
for i in range(int(num) - 1):
    a, b = b, a + b

print(b % 1000000007)