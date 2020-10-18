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


def get_matrix():
    row, column = map(int, input().split())
    matrix = [[int(i) for i in input().split()] for _ in range(row)]
    return matrix


x = get_matrix()
y = get_matrix()

# for num_list in matrix_mul(x, y):
#     for num in num_list:
#         print(num, end=' ')
#     print()
count = matrix_mul(x, y)
for i in range(len(count)):
    for j in range(len(count[0])):
        print(count[i][j], end=' ')
    print()
