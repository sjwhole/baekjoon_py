import sys

for _ in range(int(sys.stdin.readline())):
    info = sys.stdin.readline()
    score = 0
    strike = 0
    for ox in info[:-1]:
        if ox == "O":
            strike += 1
            score += strike
        else:
            strike = 0
    print(score)