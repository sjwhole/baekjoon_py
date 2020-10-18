import sys
from itertools import combinations


pass_length, info_length = map(int, sys.stdin.readline().split())


info = sys.stdin.readline().split()
info.sort()

for letters in combinations(info, pass_length):
    letter = ''.join(letters)
    vowel = 0
    for i in letter:
        if i in "aeiou":
            vowel += 1
    if vowel < 1 or pass_length - vowel < 2:
        continue
    print(letter)