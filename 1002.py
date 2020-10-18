def cal(w1, w2, r):
    distance = ((w1[0] - w2[0]) ** 2 + (w1[1] - w2[1]) ** 2) ** 0.5
    if distance == 0 and r[0] == r[1]:
        return -1
    elif distance == 0 and r[0] != r[1] or distance > r[0] + r[1] or distance < abs(r[0] - r[1]):
        return 0
    elif distance == r[0] + r[1] or distance == abs(r[0] - r[1]):
        return 1
    else:
        return 2

tries = int(input())
for i in range(tries):
    info = input().split()
    place1, place2, measure = [int(info[0]), int(info[1])], [int(info[3]), int(info[4])], [int(info[2]), int(info[5])]
    print(cal(place1, place2, measure))