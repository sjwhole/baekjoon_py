import sys
from itertools import combinations


heights = []
for _ in range(9):
    heights.append(int(sys.stdin.readline()))
for two_sum in combinations(heights, 2):
    if sum(two_sum) + 100 == sum(heights):
        heights.remove(two_sum[0])
        heights.remove(two_sum[1])
        break
heights.sort()
for height in heights:
    print(height)