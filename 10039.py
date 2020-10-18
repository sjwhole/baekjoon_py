import sys

data = []
for _ in range(5):
    score = int(sys.stdin.readline())
    if score < 40:
        data.append(40)
    else:
        data.append(score)
print(sum(data) // len(data))