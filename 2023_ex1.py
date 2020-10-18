import sys

sys.setrecursionlimit(100000000)

# def input():
#     return sys.stdin.readline()[:-1]


arr = [[2, 3, 5, 7], [], [], [], [], [], [], []]
for i in range(1, 8):
    for e in arr[i-1]:
        for j in range(1, 10):
            num = e*10+j
            for k in range(2, int(num**0.5)+1):
                if num%k == 0:
                    break
            else:
                arr[i].append(num)
print(arr)
N = int(input())
for e in arr[N-1]:
    print(e)
