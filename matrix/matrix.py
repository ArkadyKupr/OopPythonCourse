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

    def set_string_vector(self, vector, index):
        if index >= len(self.__matrix):
            raise ValueError

        matrix_width = len(self.__matrix[0])

        if len(vector) != matrix_width:
            raise ValueError

        for i in range(matrix_width):
            self.__matrix[index][i] = vector[i]

        return self.__matrix

    # 3. b) Умножение на скаляр
    def get_multiplied_matrix(self, scalar):
        matrix_length = len(self.__matrix)
        matrix_width = len(self.__matrix[0])

        for i in range(matrix_length):
            for j in range(matrix_width):
                self.__matrix[i][j] *= scalar

        return self.__matrix

    # 3. c) Прибавление к матрице другой матрицы:
    def summarize(self, other):
        matrix_1_length = len(self.__matrix)
        matrix_1_width = len(self.__matrix[0])

        matrix_2_length = len(other.__matrix)
        matrix_2_width = len(other.__matrix[0])

        if matrix_1_length != matrix_2_length and matrix_1_width != matrix_2_width:
            raise ValueError

        for i in range(matrix_1_length):
            for j in range(matrix_1_width):
                self.__matrix[i][j] += other.__matrix[i][j]

        return self.__matrix

    # 3. d) Вычитание из матрицы другой матрицы:
    def subtract(self, other):
        matrix_1_length = len(self.__matrix)
        matrix_1_width = len(self.__matrix[0])

        matrix_2_length = len(other.__matrix)
        matrix_2_width = len(other.__matrix[0])

        if matrix_1_length != matrix_2_length and matrix_1_width != matrix_2_width:
            raise ValueError

        for i in range(matrix_1_length):
            for j in range(matrix_1_width):
                self.__matrix[i][j] -= other.__matrix[i][j]

        return self.__matrix

    # 3. e) Прибавление к матрице другой матрицы:
    def get_sum_matrix(self, other):
        matrix_1_length = len(self.__matrix)
        matrix_1_width = len(self.__matrix[0])

        matrix_2_length = len(other.__matrix)
        matrix_2_width = len(other.__matrix[0])

        if matrix_1_length != matrix_2_length and matrix_1_width != matrix_2_width:
            raise ValueError

        sum_matrix = []

        for i in range(matrix_1_length):
            sum_matrix.append(matrix_1_width * [0])

        for i in range(matrix_1_length):
            for j in range(matrix_1_width):
                sum_matrix[i][j] = self.__matrix[i][j] + other.__matrix[i][j]

        return sum_matrix

    # 3. f) Вычитание матриц:
    def get_subtracted_matrix(self, other):
        matrix_1_length = len(self.__matrix)
        matrix_1_width = len(self.__matrix[0])

        matrix_2_length = len(other.__matrix)
        matrix_2_width = len(other.__matrix[0])

        if matrix_1_length != matrix_2_length and matrix_1_width != matrix_2_width:
            raise ValueError

        subtracted_matrix = []

        for i in range(matrix_1_length):
            subtracted_matrix.append(matrix_1_width * [0])

        for i in range(matrix_1_length):
            for j in range(matrix_1_width):
                subtracted_matrix[i][j] = self.__matrix[i][j] - other.__matrix[i][j]

        return subtracted_matrix

    # 3. g) Умножение матриц:
    def get_multiplication(self, other):
        matrix_1_length = len(self.__matrix)
        matrix_2_length = len(other.__matrix)

        multiplication_matrix = []

        for i in range(matrix_1_length):
            multiplication_matrix.append(matrix_1_length * [0])

        for i in range(matrix_1_length):
            for j in range(matrix_1_length):
                for k in range(matrix_2_length):
                    multiplication_matrix[i][j] += self.__matrix[i][k] * other.__matrix[k][j]

        return multiplication_matrix

    # 3. h) Умножение матрицы на вектор-столбец:
    def get_multiplication_vector(self, vector):
        matrix_length = len(self.__matrix)
        matrix_width = len(self.__matrix[0])

        vector_length = len(vector)

        multiplied_vector = []

        for i in range(matrix_length):
            multiplied_vector.append(0)

        if vector_length != matrix_width:
            raise ValueError

        for i in range(matrix_length):
            for j in range(matrix_width):
                multiplied_vector[i] += self.__matrix[i][j] * vector[j]

        return multiplied_vector

    # 3. i) Переопределить методы __eq__ и __hash__:
    def __eq__(self, other):
        if other.__matrix.__hash__ != self.__matrix.__hash__:
            return False

        matrix_1_length = len(self.__matrix)
        matrix_2_length = len(other.__matrix)

        matrix_1_width = len(self.__matrix[0])
        matrix_2_width = len(other.__matrix[0])

        if matrix_1_length == matrix_2_length and matrix_1_width == matrix_2_width:
            for i in range(matrix_1_length):
                for j in range(matrix_1_width):
                    if self.__matrix[i][j] != other.__matrix[i][j]:
                        return False

            return True

        return False

    def __hash__(self):
        return hash(self.__matrix)

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

    # 4. а) Получение вектора-столбца по индексу:
    def get_column_vector(self, index):
        n = len(self.__matrix)
        m = len(self.__matrix[0])

        if index >= m:
            raise ValueError

        column_vector = []

        for i in range(n):
            column_vector.append(self.__matrix[i][index])

        return column_vector

    # 4. b) Транспонирование матрицы:
    def transpose(self):
        n = len(self.__matrix)
        m = len(self.__matrix[0])

        multiplication_matrix = []

        for i in range(m):
            multiplication_matrix.append(n * [0])

        for i in range(n):
            for j in range(m):
                multiplication_matrix[j][i] = self.__matrix[i][j]

        return multiplication_matrix

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

                    for i in range(1, size):
                        for j in range(0, k):
                            intermediate_matrix[i - 1][j] = matrix[i][j]

                        for j in range(k + 1, size):
                            intermediate_matrix[i - 1][j - 1] = matrix[i][j]

                    determinant += pow(-1, k) * matrix[0][k] * calculate_determinant_1(intermediate_matrix)

                return determinant

        return calculate_determinant_1(self.__matrix)
