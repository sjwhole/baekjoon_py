import sys


def back_tracing(idx):
    for i in range(1, idx // 2 + 1):
        if good[-i:] == good[-i * 2: -i]:
            return False
    if idx == N:
        for num in good:
            print(num, end="")
        return True
    for i in range(1, 4):
        good.append(i)
        if back_tracing(idx + 1):
            return True
        good.pop()


N = int(sys.stdin.readline())
good = []
back_tracing(0)
