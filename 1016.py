import sys

start, end = map(int, sys.stdin.readline().split())

check_list = [True for _ in range(int(1000001))]

i = 1
square_list = [4]
while ((2 * i) + 1) ** 2 <= end:
    square_list.append(((2 * i) + 1) ** 2)
    i += 1
for square in square_list:
    num = square - start
    if num < 0:
        num += square * (abs(num) // square + 1)
        if num % square == 0:
            num -= square
    for jump in range(num, end - start + 1, square):
        check_list[jump] = False
print(check_list[:end - start + 1].count(True))