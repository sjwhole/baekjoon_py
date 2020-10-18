import sys


word = sys.stdin.readline()[:-1]
count = [-1] * 26
for i in range(97, 123):
    try:
        count[i - 97] = word.index(chr(i))
    except ValueError:
        pass
for j in count:
    print(j, end=" ")