import sys


def mod_10(n):
    remainder = n % 10
    if remainder < 6:
        return remainder
    else:
        return remainder - 10


def cal(n, s):
    if n == 0:
        return 10
    if abs(n) == 5:
        return 5
    if s % 2 == 0:
        if abs(n) == 1:
            return 1
        if abs(n) == 4:
            return 6
        four_remainder = s % 4
        if abs(n) == 2:
            return two_list[four_remainder - 1]
        if abs(n) == 3:
            return three_list[four_remainder - 1]
    else:
        if n == 1:
            return 1
        if n == -1:
            return 9
        if n == 4:
            return 4
        if n == -4:
            return 6
        four_remainder = s % 4
        if n == 2:
            return two_list[four_remainder - 1]
        if n == -2:
            return two_list[four_remainder - 1] * -1 + 10
        if n == 3:
            return three_list[four_remainder - 1]
        if n == -3:
            return three_list[four_remainder - 1] * -1 + 10


two_list = [2, 4, 8, 6]
three_list = [3, 9, 7, 1]

T = int(sys.stdin.readline())
for i in range(T):
    num, square_time = map(int, sys.stdin.readline().split())
    print(cal(mod_10(num), square_time))