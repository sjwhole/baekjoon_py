import sys
import time


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


digit = sys.stdin.readline()
start = time.time()
for num in range(int("1" + "0" * (int(digit) - 1)) + 1, int("1" + "0" * int(digit)), 2):
    if not is_prime(num):
        continue
    prime = True
    for i in range(1, int(digit)):
        if not is_prime(int(str(num)[:-i])):
            prime = False
            break
    if prime:
        print(num)

print(time.time() - start)
