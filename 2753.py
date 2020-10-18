import sys


def is_leap_year(year):
    if year % 400 == 0:
        return 1
    if year % 4 == 0 and year % 100 != 0:
        return 1
    else:
        return 0


print(is_leap_year(int(sys.stdin.readline())))
