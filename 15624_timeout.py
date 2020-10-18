import sys
import time

num = sys.stdin.readline()
start = time.time()

arr = [[] for _ in range(10000001)]
arr[0] = [0]
arr[1] = [1]

for i in range(int(num) - 1):
    arr[i + 2].append(arr[i + 1][0] + arr[i][0])

print(arr[int(num)][0] % 1000000007)
print(time.time() - start)