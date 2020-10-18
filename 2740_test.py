def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        temp_row = []
        for j in range(0, len(arr2[0])):
            value = 0
            for k in range(0, len(arr1[0])):
                value += arr1[i][k] * arr2[k][j]
            temp_row.append(value)
        answer.append(temp_row)
    return answer


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
count = solution(x, y)
for i in range(len(count)):
    for j in range(len(count[0])):
        print(count[i][j], end=' ')
    print()
