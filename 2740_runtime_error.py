def matrix_mul(a, b):
    result = [[0 for _ in range(len(a))] for _ in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def get_matrix():
    row, column = map(int, input().split())
    matrix = [[int(i) for i in input().split()] for _ in range(row)]
    return matrix


x = get_matrix()
y = get_matrix()

count = matrix_mul(x, y)
for i in range(len(count)):
    for j in range(len(count[0])):
        print(count[i][j], end=' ')
    print()