from multipledispatch import dispatch
from vector_task.vector import Vector


class Matrix:
    # 1. а) Конструктор: матрица нулей m x n, где m - rows, а n - columns
    @dispatch(int, int)
    def __init__(self, rows_quantity, columns_quantity):
        if not isinstance(rows_quantity, int):
            raise TypeError(f"Тип rows_quantity: {rows_quantity}, не является int")

        if rows_quantity <= 0:
            raise ValueError("Количество строк должно быть больше нуля. "
                             f"Сейчас передано значение rows_quantity: {rows_quantity}")

        if not isinstance(columns_quantity, int):
            raise TypeError(f"Тип columns_quantity: {columns_quantity}, не является int")

        if columns_quantity <= 0:
            raise ValueError("Количество столбцов должно быть больше нуля. "
                             f"Сейчас передано значение columns_quantity: {columns_quantity}")

        self.__rows = []

        for i in range(rows_quantity):
            self.__rows.append(Vector(columns_quantity))

    # 1. b) Конструктор: конструктор копирования с проверкой, что передан объект
    @dispatch(object)
    def __init__(self, matrix):
        if not isinstance(matrix, Matrix):
            raise TypeError(f"Объект matrix: {matrix}, не является объектом класса Matrix")

        self.__rows = []

        for i in range(matrix.rows_quantity):
            self.__rows.append(Vector(matrix[i]))

    # 1. с) Конструктор: из двумерного списка чисел
    # 1. d) Конструктор: из списка векторов-строк
    @dispatch(list)
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise TypeError(f"Тип elements: {elements}, не является list")

        rows_quantity = len(elements)

        # Проверка, что размер создаваемой матрицы > 0
        if rows_quantity == 0:
            raise ValueError(f"Размер матрицы elements: {elements}, должен быть > 0")

        if isinstance(elements[0], list):
            # Проверка, что все элементы из двумерного списка имеют тип list
            for row in elements:
                if not isinstance(row, list):
                    raise TypeError("Тип одного из элементов не является list. Однако, тип всех элементов"
                                    " должен быть list")

                # Проверка, что каждый элемент списка - это список чисел
                for component in row:
                    if not isinstance(component, (int, float)):
                        raise TypeError(f"Строка матрицы row: {row}, не является списком чисел")

            max_row_dimension = len(elements[0])

            # Получение размера максимальной строки в elements
            for row in elements:
                max_row_dimension = max(len(row), max_row_dimension)

            # Копирование аргумента elements c увеличением размеров всех векторов до max_row_dimension
            self.__rows = []

            for i in range(rows_quantity):
                self.__rows.append(Vector(max_row_dimension))

                self.__rows[i] += Vector(elements[i])
        elif isinstance(elements[0], Vector):
            # Проверка, что все элементы из списка векторов-строк имеют тип Vector
            for i in range(1, rows_quantity):
                if not isinstance(elements[i], Vector):
                    raise TypeError("Один из элементов списка не является объектом Vector. Однако, все элементы"
                                    " должны быть объектами Vector")

            # Проверка, что все объекты Vector имеют одну размерность
            max_vector_dimension = elements[0].dimension

            for vector in elements:
                max_vector_dimension = max(vector.dimension, max_vector_dimension)

            # Копирование аргумента elements c увеличением размеров всех векторов до max_vector_dimension
            self.__rows = []

            for i in range(rows_quantity):
                self.__rows.append(Vector(max_vector_dimension))

                self.__rows[i] += elements[i]
        else:
            raise TypeError("Тип первого элемента списка не является ни list, ни объектом Vector")

    # 2. Свойства: получение размеров матрицы
    @property
    def rows_quantity(self):
        return len(self.__rows)

    @property
    def columns_quantity(self):
        return len(self.__rows[0])

    # 3. а) Получение и задание вектора-строки по индексу
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип {index} должен быть int")

        if index < -self.rows_quantity or index >= self.rows_quantity:
            raise IndexError(f"Заданный индекс вектора-строки: {index}, должен быть в диапазоне "
                             f"[{-self.rows_quantity}, {self.rows_quantity - 1}]")

        copied_vector = self.__rows[index]

        return copied_vector

    # 4. а) Получение вектора-столбца по индексу:
    def get_column(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип index: {index}, должен быть int")

        if index < -self.columns_quantity or index >= self.columns_quantity:
            raise IndexError(f"Заданный индекс вектора-столбца index: {index}, должен быть в диапазоне: "
                             f"[{-self.columns_quantity}, {self.columns_quantity - 1}].")

        column_list = []

        for i in range(self.rows_quantity):
            column_list.append(self.__rows[i][index])

        return Vector(column_list)

    def __len__(self):
        return len(self.__rows)

    def __setitem__(self, index, row_vector):
        if not isinstance(index, int):
            raise TypeError(f"Тип index: {index}, должен быть int")

        if not isinstance(row_vector, Vector):
            raise TypeError(f"Тип row_vector: {row_vector}, должен быть Vector")

        if index < -self.rows_quantity or index >= self.rows_quantity:
            raise IndexError(f"Заданный индекс вектора-строки index: {index}, должен быть в диапазоне: "
                             f"[{-self.rows_quantity}, {self.rows_quantity - 1}]")

        self.__rows[index] = Vector(row_vector)

    # 3. b) Умножение на скаляр
    def __imul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Тип scalar: {scalar}, должен быть int иди float")

        for row_vector in self:
            row_vector *= scalar

        return self

    # Сравнение размерностей двух матриц и бросание исключения
    def __check_dimensions_equality(self, other):
        if self.rows_quantity != other.rows_quantity or self.columns_quantity != other.columns_quantity:
            raise ValueError(f"Размеры двух матриц: первой матрицы {self.rows_quantity}x{self.columns_quantity} и "
                             f"второй - {other.rows_quantity}x{other.columns_quantity}, не равны")

    # 3. c) Прибавление к матрице другой матрицы:
    def __iadd__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        self.__check_dimensions_equality(other)

        for i in range(self.rows_quantity):
            self.__rows[i] += other.__rows[i]

        return self

    # 3. d) Вычитание из матрицы другой матрицы:
    def __isub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        self.__check_dimensions_equality(other)

        for i in range(self.rows_quantity):
            self.__rows[i] -= other.__rows[i]

        return self

    # 3. e) Прибавление к матрице другой матрицы:
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        self.__check_dimensions_equality(other)

        matrices_sum = Matrix(self)
        matrices_sum += other

        return matrices_sum

    # 3. f) Вычитание матриц:
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        self.__check_dimensions_equality(other)

        matrices_difference = Matrix(self)
        matrices_difference -= other

        return matrices_difference

    # 3. g) Умножение матриц:
    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        # Проверка размеров матриц в соответствии с правилами умножения матриц
        if self.columns_quantity != other.rows_quantity:
            raise ValueError(f"Количество столбцов первой матрицы {self.rows_quantity}x{self.columns_quantity} должно "
                             f"быть равно количеству строк второй - {other.rows_quantity}x{other.columns_quantity}")

        product = [[0] * other.columns_quantity for _ in range(self.rows_quantity)]

        # Было: product = [[0 for _ in range(other.columns_quantity)] for _ in range(self.rows_quantity)]

        for i in range(self.rows_quantity):
            for j in range(other.columns_quantity):
                for k in range(other.rows_quantity):
                    product[i][j] += self.__rows[i][k] * other.__rows[k][j]

        return Matrix(product)

    # 3. h) Умножение матрицы на вектор-столбец:
    def multiply_by_vector(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError(f"Объект {vector} не является объектом класса Vector."
                            f"Вместо этого передан тип {type(vector).__name__}")

        if vector.dimension != self.columns_quantity:
            raise ValueError(f"Размерность вектора {vector}: {vector.dimension}, должна "
                             f"быть равна количеству столбцов матрицы - {self}: {self.columns_quantity}")

        return Vector([Vector.get_scalar_product(row, vector) for row in self.__rows])

    # 3. i) Переопределить методы __eq__ и __hash__:
    def __hash__(self):
        return hash(tuple(self.__rows))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return other.__rows == self.__rows

    # 4. d) Метод __repr__ определить, чтобы результат был в виде: {{1, 2}, {2, 3}}
    def __repr__(self):
        strings_lists = map(str, self.__rows)

        return "{" + ", ".join(strings_lists) + "}"

    # 4. b) Транспонирование матрицы:
    # https://docs.python.org/2/tutorial/datastructures.html
    def transpose(self):
        self.__rows = [self.get_column(i) for i in range(self.columns_quantity)]

        # self.__rows = [Vector([row[i] for row in self.__rows]) for i in range(self.columns_quantity)]

    # 4. c) Вычисление определителя матрицы:
    def get_determinant(self):
        if self.columns_quantity != self.rows_quantity:
            raise ValueError("Количество строк матрицы должно быть равно количеству столбцов. "
                             f"Сейчас размеры матрицы: {self.rows_quantity}x{self.columns_quantity}")

        def get_determinant_inner(matrix):
            size = len(matrix[0])

            if size == 1:
                return matrix[0][0]

            if size == 2:
                return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

            determinant = 0

            for k in range(size):
                minor = []

                for i in range(size - 1):
                    minor.append((size - 1) * [0])

                for i in range(1, size):
                    for j in range(k):
                        minor[i - 1][j] = matrix[i][j]

                    for j in range(k + 1, size):
                        minor[i - 1][j - 1] = matrix[i][j]

                determinant += pow(-1, k) * matrix[0][k] * get_determinant_inner(minor)

            return determinant

        return get_determinant_inner(self.__rows)
