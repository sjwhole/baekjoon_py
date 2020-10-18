import time

def isss(n):
    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False
    return True
def sosu(n, m):
    if n == 1:
        print(m)
    else:
        m *= 10
        for i in [1, 3, 7, 9]:
            if isss(m + i) == True:
                sosu(n - 1, m + i)
            else:
                continue
n = int(input())
start = time.time()
for i in [2, 3, 5, 7]:
    sosu(n, i)

print(f"소요 시간 : {time.time() - start}")