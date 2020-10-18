import sys
import time


def sieve(start, end):
    a = [False, False] + [True] * (end - 1)
    primes = []

    for i in range(2, start):
        if a[i]:
            for j in range(2 * i, end + 1, i):
                a[j] = False
    for i in range(start, end + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, end + 1, i):
                a[j] = False
    return a, primes


digit = sys.stdin.readline()
start = time.time()
check_list, num_list = sieve(int("1" + "0" * (int(digit) - 1)) + 1, int("1" + "0" * int(digit)))
for num in num_list:
    prime = True
    for i in range(1, int(digit)):
        if not check_list[int(str(num)[:-i])]:
            prime = False
            break
    if prime:
        print(num)

print(time.time() - start)
