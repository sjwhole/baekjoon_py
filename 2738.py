def matrix_add(a, b):
    result = []
    for i in range(len(a)):
        temp = []
        for j in range(len(b[0])):
            temp.append(a[i][j] + b[i][j])
        result.append(temp)
    return result


def get_matrix():
    matrix = [[int(i) for i in input().split()] for _ in range(row)]
    return matrix


row, column = map(int, input().split())
x = get_matrix()
y = get_matrix()

count = matrix_add(x, y)
for i in range(len(count)):
    for j in range(len(count[0])):
        print(count[i][j], end=' ')
    print()