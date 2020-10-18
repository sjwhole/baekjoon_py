import sys

num_list = []
length = int(sys.stdin.readline())
for _ in range(length):
    num_list.append(int(sys.stdin.readline()))

for i in range(1, length // 2 + 1):
    print(num_list.index(i))
    num_list.remove(i)
    print(length - num_list.index(length - i + 1) - (2 * i - 1) - 1)
    num_list.remove(length - i + 1)

if length % 2 != 0:
    print(0)