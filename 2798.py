import sys
from itertools import combinations

length, target = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
score = []
for hab in combinations(data, 3):
    add = sum(hab)
    if add <= target:
        score.append(add)
print(max(score))
