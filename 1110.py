import sys

num = int(sys.stdin.readline())
num_origin = num
i = 0
while True:
    i += 1
    if num < 10:
        num = int(str(num) * 2)
    else:
        num = int((str(num)[-1]) + str(int(str(num)[-2]) + int(str(num)[-1]))[-1])
    if num == num_origin:
        print(i)
        break
