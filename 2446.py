import sys

num = int(sys.stdin.readline())
for i in range(num, 0, -1):
    print(f"{' ' * (num - i)}{'*' * (2 * i - 1)}")
for j in range(2, num + 1):
    print(f"{' ' * (num - j)}{'*' * (2 * j - 1)}")
