from matrix import Matrix

user_matrix = Matrix(2, 5)
print(user_matrix)

user_matrix_1 = Matrix([[1, 2], [3, 6], [3, 6]])
print(user_matrix_1)

user_matrix_2 = Matrix([(1, 2), (3, 6), (5, 7)])
print(user_matrix_2)

user_matrix_3 = Matrix(["1, 2", "3, 6", "5, 7"])
print(user_matrix_3)

print("Размер матрицы:", user_matrix_1.matrix_dimensions)

print("Получение вектора-строки по индексу:", user_matrix.get_string_vector(1))

print("Задание вектора-строки по индексу:", user_matrix_1.set_string_vector([1, 4], 1))

print("Умножение на скаляр:", user_matrix_1.get_multiplied_matrix(100))

user_matrix_1 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_4 = Matrix([[1, 2, 5], [3, 6, 2]])

print("Умножение двух матриц:", user_matrix_1.get_multiplication(user_matrix_4))

print("Получить вектор-столбец:", user_matrix_4.get_column_vector(2))

user_matrix_5 = Matrix([[1, 1, 80, 12], [1, 3, 3, 45], [3, 4, 6, 0], [4, 8, 45, 87]])
print(user_matrix_5)

user_matrix_6 = Matrix([[1, 1, 80, 12], [1, 3, 3, 45], [3, 4, 6, 0]])
print("Транспонирование матрицу:", user_matrix_6.transpose())

determinant = user_matrix_5.calculate_determinant()
print("Вычисление определителя матрицы:", determinant)

user_matrix_7 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_8 = Matrix([(1, 2), (3, 6), (5, 7)])
print("Прибавление к матрице другой матрицы:", user_matrix_7.summarize(user_matrix_8))

user_matrix_9 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_10 = Matrix([[1, 2], [3, 6], [5, 7]])
print("Вычитание из матрицы другой матрицы:", user_matrix_9.subtract(user_matrix_10))

user_matrix_9 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_10 = Matrix([[1, 2], [3, 6], [5, 7]])
print("Сложение матриц:", user_matrix_9.get_sum_matrix(user_matrix_10))
print("Вычитание матриц:", user_matrix_9.get_subtracted_matrix(user_matrix_10))

user_matrix_11 = Matrix([[1, 2], [3, 6], [3, 6]])
print("Умножение матрицы на вектор-столбец:", user_matrix_11.get_multiplication_vector([1, 2]))

user_matrix_12 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_13 = Matrix([[1, 2], [3, 6], [3, 6]])
print("Переопределить метод __eq__:", user_matrix_12.__eq__(user_matrix_13))
print("Переопределить метод __hash__:", user_matrix_13.__hash__)
