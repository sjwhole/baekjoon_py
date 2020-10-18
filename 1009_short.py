for i in range(int(input())):
    n = pow(*map(int, input().split()), 10)
    print(10 if n == 0 else n)
