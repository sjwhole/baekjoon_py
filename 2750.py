import sys

data = []
for _ in range(int(sys.stdin.readline())):
    data.append(int(sys.stdin.readline()))
data.sort()

for num in data:
    print(num)