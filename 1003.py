def fibo(n):
    ls = [[1, 0], [0, 1]] + [[0, 0] for i in range(39)]
    for i in range(n-1):
        ls[i + 2][0] = ls[i + 1][0] + ls[i][0]
        ls[i + 2][1] = ls[i + 1][1] + ls[i][1]
    return ls[n][0], ls[n][1]

tries = int(input())
for i in range(tries):
    num = int(input())
    x, y = fibo(num)
    print(f"{x} {y}")
