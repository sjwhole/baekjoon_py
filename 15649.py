import sys
from itertools import permutations

num, length = map(int, sys.stdin.readline().split())
numlist = [str(i) for i in range(1, num + 1)]
for nums in permutations(numlist, length):
    print(' '.join(nums))