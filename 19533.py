import sys
from math import log10, pow


def prt_str(x, y):
    length = int(log10(x) + y) + 1
    mod_list = [1, 2, 0] + [1] * (length - 2)
    str_list = ["-2-4-6-8-11-14-17", "1-3-5-7-9-12-15-1...", "1-3-5-7-10-13-16-..."]
    mod = int(x * pow(10, y) % (length + 1))
    idx = mod_list[mod]
    print(str_list[idx])


for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    prt_str(a, b)
