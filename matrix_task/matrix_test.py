from matrix_task.matrix import Matrix
from vector_task.vector import Vector

print("# 1. a) Конструктор: матрица нулей m x n, где m - rows, а n - columns:")
user_matrix_1 = Matrix(1, 3)
print(user_matrix_1)
print()

print("# 1. b) Конструктор: конструктор копирования:")
user_matrix_2 = Matrix(user_matrix_1)
print(user_matrix_2)
print()

print("# 1. с) Конструктор: из двумерного списка чисел:")
user_matrix_3 = Matrix([[1, 2, 0, 0], [3, 6], [5, 7], [0]])
print(user_matrix_3)
print()

print("# 1. d) Конструктор: из списка векторов-строк:")
user_matrix_4 = Matrix([Vector([1, 9, 0, 10, 0, 9, 10]),
                        Vector([1, 9, 0, 10]),
                        Vector([1, 9, 0, 10]),
                        Vector([1, 9, 0, 10])])
print(user_matrix_4)
print()

print("# 2. Свойства: получение размеров матрицы:")
print("Количество строк:", user_matrix_1.rows_quantity)
print("Количество столбцов:", user_matrix_1.columns_quantity)
print()

print("# 3. а) Получение и задание вектора-строки по индексу:")
print("Получение вектора-строки по индексу:", user_matrix_4[-4])
print()

print("Получение вектора-столбца по индексу:", user_matrix_4.get_column(-7))

user_matrix_1[0] = Vector([0, 1])
user_matrix_4[-4] = Vector([0, 1, 6, 7])
print("Задание вектора-строки по индексу:", user_matrix_1)
print("Задание вектора-строки по индексу:", user_matrix_4)
print()

print("# 3. b) Умножение на скаляр:")
user_matrix_4 *= 4.2
print(user_matrix_4)
print()

print("# 3. c) Прибавление к матрице другой матрицы:")
user_matrix_5 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_6 = Matrix([[1, 2], [3, 6], [5, 7]])
user_matrix_5 += user_matrix_6
print(user_matrix_5)
print()

print("# 3. d) Вычитание из матрицы другой матрицы:")
user_matrix_7 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_8 = Matrix([[1, 2], [3, 6], [5, 7]])
user_matrix_7 += user_matrix_8
print(user_matrix_7)
print()

print("# 3. e) Прибавление к матрице другой матрицы:")
user_matrix_9 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_10 = Matrix([[1, 2], [3, 6], [5, 7]])
print(user_matrix_9 + user_matrix_10)
print()
print("# 3. f) Вычитание матриц:")
print(user_matrix_9 - user_matrix_10)
print()

print("# 3. g) Умножение матриц:")
user_matrix_11 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_12 = Matrix([[1, 2, 5, 7], [3, 6, 2, 7]])
print(user_matrix_11 * user_matrix_12)
print()

print("# 3. h) Умножение матрицы на вектор-столбец:")
user_matrix_13 = Matrix([[1, 2], [3, 6], [3, 6]])
print(user_matrix_13.multiply_by_vector(Vector([1, 9])))
print()

print("# 3. i) Переопределить методы __eq__ и __hash__:")
user_matrix_14 = Matrix([[1, 2], [3, 6], [3, 6]])
user_matrix_15 = Matrix([[1, 2], [3, 6, 0], [3, 6]])
print("Переопределить метод __eq__:", user_matrix_14 == user_matrix_15)
print("Переопределить метод __hash__:", hash(user_matrix_15))
print()

print("# 4. а) Получение вектора-столбца по индексу:")
user_matrix_16 = Matrix([[1, 1, 80, 12], [1, 3, 3, 45], [3, 4, 6, 0], [4, 8, 45, 87]])
print(user_matrix_16.get_column(2))
print()

print("# 4. b) Транспонирование матрицы:")
user_matrix_17 = Matrix([[1, 1, 80, 12], [1, 3, 3, 45]])
Matrix.transpose(user_matrix_17)
print(user_matrix_17)
print()

print("# 4. c) Вычисление определителя матрицы:")
user_matrix_18 = Matrix([[1, 1, 80], [1, 3, 3], [3, 4, 6]])
determinant = user_matrix_18.get_determinant()
print(determinant)
print()

user_matrix_19 = Matrix([[1]])
determinant = user_matrix_19.get_determinant()
print(determinant)
