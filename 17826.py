import sys

score = list(map(int, sys.stdin.readline().split()))
rank = score.index(int(sys.stdin.readline())) + 1

if rank <= 5:
    print("A+")
elif 5 < rank <= 15:
    print("A0")
elif 15 < rank <= 30:
    print("B+")
elif 30 < rank <= 35:
    print("B0")
elif 35 < rank <= 45:
    print("C+")
elif 45 < rank <= 48:
    print("C0")
else:
    print("F")