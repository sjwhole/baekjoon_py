import sys


def fibo(n):
    sqrt_5 = 5 ** (1/2)
    ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )
    return int(ans)


num = sys.stdin.readline()
print(fibo(int(num)) % 1000000007)