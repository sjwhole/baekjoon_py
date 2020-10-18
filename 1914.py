import sys
from math import pow


def hanoi(n, start, end, mid):
    if n == 1:
        print(f"{start} {end}")
        return
    hanoi(n - 1, start, mid, end)
    print(f"{start} {end}")
    hanoi(n - 1, mid, end, start)


N = int(sys.stdin.readline())
print(int(pow(2, N)) - 1)
if N < 21:
    hanoi(N, 1, 3, 2)