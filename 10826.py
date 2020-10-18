import sys

same = [[1, 0], [0, 1]]
main = [[1, 1], [1, 0]]


def matrix_mul(a, b):
    result = []
    for i in range(len(a)):
        temp = []
        for j in range(len(b[0])):
            value = 0
            for k in range(len(b)):
                value += a[i][k] * b[k][j]
            temp.append(value)
        result.append(temp)
    return result


def ntime_square(n):
    matrix = same.copy()
    k = 0
    tmp = main.copy()

    while 2 ** k <= n:
        if n & (1 << k) != 0:
            matrix = matrix_mul(matrix, tmp)
        k += 1
        tmp = matrix_mul(tmp, tmp)
    return matrix


n = sys.stdin.readline()
fibo = ntime_square(int(n))[0][1]
print(fibo)