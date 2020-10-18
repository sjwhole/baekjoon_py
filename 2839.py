import sys

sugar = int(sys.stdin.readline())

i = sugar // 5
while i >= 0:
    if (sugar - (5 * i)) % 3 == 0:
        three = (sugar - (5 * i)) // 3
        print(i + three)
        break
    elif i == 0:
        print("-1")
    i -= 1