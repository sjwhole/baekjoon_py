import sys

count = int(sys.stdin.readline())
data = [0] * 10001

for _ in range(count):
    num = int(sys.stdin.readline())
    data[num] += 1
for i in range(10001):
    if data[i] != 0:
        for _ in range(data[i]):
            print(i)