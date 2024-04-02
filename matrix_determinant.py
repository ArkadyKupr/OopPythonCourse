def create_matrix(size):
    matrix = []

    for i in range(size):
        matrix.append(size * [0])

    for i in range(size):
        for j in range(size):
            if i == 1 and j == 1:
                matrix[i][j] = -5
            elif i == 2 and j == 1:
                matrix[i][j] = 3
            else:
                matrix[i][j] = 1

    return matrix


def calculate_determinant(matrix):
    size = len(matrix[0])
    determinant = 0

    if size == 1:
        determinant = matrix[0][0]
    elif size == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        for k in range(size):
            intermediate_matrix = create_matrix(size - 1)
            for i in range(1, size):
                for j in range(0, k):
                    intermediate_matrix[i - 1][j] = matrix[i][j]
                for j in range(k + 1, size):
                    intermediate_matrix[i - 1][j - 1] = matrix[i][j]

            determinant += pow(-1, k) * matrix[0][k] * calculate_determinant(intermediate_matrix)

    return determinant


def get_sum_of_two_matrix(matrix_1, matrix_2):
    matrix_1_length = len(matrix_1)
    matrix_2_length = len(matrix_2)

    sum_matrix = []

    for i in range(matrix_1_length):
        sum_matrix.append(matrix_2_length * [0])

    for i in range(matrix_1_length):
        for j in range(matrix_2_length):
            sum_matrix[i][j] += matrix_1[i][j] * matrix_2[j][i]

    return sum_matrix


def transpose_matrix(matrix):
    #матрица m x n
    m = len(matrix[0])
    n = len(matrix)

    for i in range(m):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


user_matrix = create_matrix(3)
print(user_matrix)

print(calculate_determinant(user_matrix))
print(transpose_matrix(user_matrix))
print(transpose_matrix(user_matrix))

matrix_1 = [[2, 3, 4], [2, 3, 5]]
matrix_2 = [[2, 3], [2, 3], [2, 3]]
print(get_sum_of_two_matrix(matrix_1, matrix_2))
