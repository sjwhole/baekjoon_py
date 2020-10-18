import sys

start, end = map(int, sys.stdin.readline().split())

count = 0
for num in range(start, end + 1):
    i = 2
    sqare_nono = True
    while i * i <= num:
        if num % (i * i) == 0:
            sqare_nono = False
            break
        i += 1
    if sqare_nono:
        count += 1
print(count)