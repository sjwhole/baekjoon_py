def matrix(a, b):
    result = [[0 for _ in range(len(a))] for _ in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


x = [[1, 2, 3, ],
     [4, 5, 6]]
y = [[1, 1],
     [1, 0],
     [0, 1]]

print(matrix(x, y))