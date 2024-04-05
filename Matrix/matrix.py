from multipledispatch import dispatch
import copy


class Matrix:
    # 1. а) Конструктор: матрица нулей m x n
    @dispatch(int, int)
    def __init__(self, n, m):
        if n <= 0 or m <= 0:
            raise ValueError

        matrix = []

        for i in range(n):
            matrix.append(m * [0])

        self.__matrix = matrix

    # 1. b) Конструктор: конструктор копирования
    @dispatch(list)
    def __init__(self, matrix):
        self.__matrix = copy.deepcopy(matrix)

    # 1. с) Конструктор: из двумерного списка чисел
    @dispatch((list, float, float))
    def __init__(self, elements):
        self.__matrix = elements

    # 1. d) Конструктор: из списка векторов-строк
    @dispatch(list, str)
    def __init__(self, vectors):
        for word in vectors:
            int(word.split(", "))

        self.__matrix = vectors

    # 2. Свойства: получение размеров матрицы
    @property
    def matrix_dimensions(self):
        n = len(self.__matrix)

        current_row = 0
        current_m = 0

        while current_row < n:
            if current_m < len(self.__matrix[current_row]):
                current_m = len(self.__matrix[current_row])

            current_row += 1

        m = current_m

        return n, m

    # 3. а) Получение и задание вектора-строки по индексу
    def get_string_vector(self, index):
        if index >= len(self.__matrix):
            raise ValueError

        return self.__matrix[index]

    # 3. b) Умножение на скаляр
    def get_multiplied_matrix(self, scalar):
        matrix_length = len(self.__matrix)
        matrix_width = len(self.__matrix[0])

        for i in range(matrix_length):
            for j in range(matrix_width):
                self.__matrix[i][j] *= scalar

        return self.__matrix

    # 3. c) Прибавление к матрицы другой матрицы:
    def get_sum_of_two_matrix(self, other):
        matrix_1_length = len(self.__matrix)
        matrix_2_length = len(other.__matrix)

        sum_matrix = []

        for i in range(matrix_1_length):
            sum_matrix.append(matrix_1_length * [0])

        for i in range(matrix_1_length):

            for j in range(matrix_1_length):

                for k in range(matrix_2_length):
                    sum_matrix[i][j] += self.__matrix[i][k] * other.__matrix[k][j]

        return sum_matrix

    # def exchange_string_vector(self, index, vector):
    # if index >= len(self.__matrix):
    # raise ValueError

    # self.__matrix[index] = vector

    # 4. d) Метод __repr__ определить, чтобы результат был в виде: {{1, 2}, {2, 3}}
    def __repr__(self):
        quantity = len(self.__matrix)

        numbers_string = "{"

        for i, vector in enumerate(self.__matrix):
            vector_size = len(self.__matrix[i])

            numbers_string += "{"

            for j, vector_item in enumerate(self.__matrix[i]):
                numbers_string += str(vector_item)

                if j != vector_size - 1:
                    numbers_string += ", "
                else:
                    numbers_string += "}"

            if i != quantity - 1:
                numbers_string += ", "

        numbers_string += "}"

        return f"{numbers_string}"

    # 4. c) Вычисление определителя матрицы:
    def calculate_determinant(self):
        m = len(self.__matrix)
        n = len(self.__matrix[0])

        if n == 0 or m == 0 or n != m:
            raise ValueError

        if n == 1:
            return self.__matrix[0][0]
        if n == 2:
            return self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]

        def calculate_determinant_1(matrix):
            size = len(matrix[0])

            if size == 1:
                return matrix[0][0]
            elif size == 2:
                return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            else:
                determinant = 0

                for k in range(size):
                    intermediate_matrix = []

                    for i in range(size - 1):
                        intermediate_matrix.append((size - 1) * [0])
                        print(intermediate_matrix)

                    for i in range(1, size):
                        for j in range(0, k):
                            intermediate_matrix[i - 1][j] = matrix[i][j]

                        for j in range(k + 1, size):
                            intermediate_matrix[i - 1][j - 1] = matrix[i][j]

                    print(":", intermediate_matrix)

                    determinant += pow(-1, k) * matrix[0][k] * calculate_determinant_1(intermediate_matrix)

                return determinant

        return calculate_determinant_1(self.__matrix)


user_matrix = Matrix(2, 5)
print(user_matrix)

user_matrix_1 = Matrix([[1, 2], [3, 6], [3, 6]])
print(user_matrix_1)

user_matrix_2 = Matrix([(1, 2), (3, 6), (5, 7)])
print(user_matrix_2)

user_matrix_3 = Matrix(["1, 2", "3, 6", "5, 7"])
print(user_matrix_3)

print("Размер матрицы:", user_matrix_1.matrix_dimensions)

print(user_matrix.get_string_vector(1))

print(user_matrix_1.get_multiplied_matrix(100))

user_matrix_1 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_4 = Matrix([[1, 2, 5], [3, 6, 2]])

print("Сумма векторов:", user_matrix_1.get_sum_of_two_matrix(user_matrix_4))

user_matrix_5 = Matrix([[1, 1, 80, 12], [1, 3, 3, 45], [3, 4, 6, 0], [4, 8, 45, 87]])
print(user_matrix_5)

determinant = user_matrix_5.calculate_determinant()

print("Детерминант:", determinant)
