import sys


for _ in range(int(sys.stdin.readline())):
    info = list(map(int, sys.stdin.readline().split()))
    length = info[0]
    num_list = info[1:]
    mean = sum(num_list) / length
    count = 0
    for num in num_list:
        if num > mean:
            count += 1
    print("%0.3f" %round(count / length * 100, 3) + "%")