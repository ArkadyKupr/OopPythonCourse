from multipledispatch import dispatch
import copy
from vector_task.vector import Vector


class Matrix:
    # 1. а) Конструктор: матрица нулей m x n, где m - rows, а n - columns
    @dispatch(int, int)
    def __init__(self, rows_quantity, columns_quantity):
        if not isinstance(rows_quantity, int):
            raise TypeError(f"Тип {rows_quantity} не является int")

        if rows_quantity <= 0:
            raise ValueError(f"Количество строк должно быть больше нуля. Сейчас передано значение: {rows_quantity}")

        if not isinstance(columns_quantity, int):
            raise TypeError(f"Тип {columns_quantity} не является int")

        if columns_quantity <= 0:
            raise ValueError(f"Количество столбцов должно быть больше нуля. "
                             f"Сейчас передано значение: {columns_quantity}")

        self.__rows = []

        for i in range(rows_quantity):
            self.__rows.append(Vector(columns_quantity))

    # 1. b) Конструктор: конструктор копирования с проверкой, что передан объект
    @dispatch(object)
    def __init__(self, matrix):
        if not isinstance(matrix, Matrix):
            raise TypeError(f"Объект {matrix} не является объектом класса Matrix")

        self.__rows = []

        for i in range(matrix.rows_quantity):
            self.__rows.append(Vector(matrix[i]))

    # 1. с) Конструктор: из двумерного списка чисел
    # 1. d) Конструктор: из списка векторов-строк
    @dispatch(list)
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise TypeError(f"Тип {elements} не является list")

        rows_quantity = len(elements)

        # Проверка, что размер создаваемой матрицы > 0
        if rows_quantity == 0:
            raise ValueError(f"Размер матрицы {elements} должен быть > 0")

        if isinstance(elements[0], list):
            # Проверка, что все элементы из двумерного списка имеют тип list
            for element in elements:
                if not isinstance(element, list):
                    raise TypeError(f"Тип одного из элементов не является list. Однако, тип всех элементов"
                                    f" должен быть list")

                # Проверка, что каждый список список - это список чисел
                for component in element:
                    if not isinstance(component, (int, float)):
                        raise TypeError(f"Строка матрицы: {element}, не является списком чисел")

            # Проверка, что все элементы-списки одного размера и получение размера максимального списка
            max_element_dimension = len(elements[0])
            have_different_dimensions = False

            for element in elements:
                if len(element) != max_element_dimension:
                    max_element_dimension = max(len(element), max_element_dimension)
                    have_different_dimensions = True

            if have_different_dimensions is True:
                for element in elements:
                    current_element_dimension = len(element)

                    while current_element_dimension < max_element_dimension:
                        element.append(0)
                        current_element_dimension += 1

            self.__rows = []

            for i in range(rows_quantity):
                self.__rows.append(Vector(elements[i]))

        elif isinstance(elements[0], Vector):
            # Проверка, что все элементы из двумерного списка имеют тип Vector
            for i in range(1, rows_quantity):
                if not isinstance(elements[i], Vector):
                    raise TypeError(f"Один из элементов списка не является объектом Vector. Однако, все элементы"
                                    f" должны быть объектами Vector")

            # Проверка, что все объекты Vector одного размера
            max_element_dimension = elements[0].dimension

            for element in elements:
                if len(element) != max_element_dimension:
                    max_element_dimension = max(element.dimension, max_element_dimension)

            self.__rows = []

            for i in range(rows_quantity):
                elements[i] += Vector(max_element_dimension)
                self.__rows.append(elements[i])

        else:
            raise TypeError(f"Тип первого элемента списка не является ни list, ни объектом Vector")

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

        if index < - self.rows_quantity or index >= self.rows_quantity:
            raise IndexError(f"Заданный индекс вектора-строки: {index}, должен быть в диапазоне "
                             f"[{-self.rows_quantity}, {self.rows_quantity - 1}]")

        return self.__rows[index]

    # 4. а) Получение вектора-столбца по индексу:
    def get_column(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип {index} должен быть int")

        if index < - self.columns_quantity or index >= self.columns_quantity:
            raise IndexError(f"Заданный индекс вектора-столбца: {index}, должен быть в диапазоне: "
                             f"[{-self.columns_quantity}, {self.columns_quantity - 1}].")

        column_vector = []

        for i in range(self.rows_quantity):
            column_vector.append(self.__rows[i][index])

        return Vector(column_vector)

    def __len__(self):
        return len(self.__rows)

    def __setitem__(self, index, component):
        if not isinstance(index, int):
            raise TypeError(f"Тип {index} должен быть int")

        if not isinstance(component, list):
            raise TypeError(f"Тип {component} должен быть list")

        if index < -self.rows_quantity or index >= self.rows_quantity:
            raise IndexError(f"Заданный индекс вектора-строки: {index}, должен быть в диапазоне: "
                             f"[{-self.rows_quantity}, {self.rows_quantity - 1}]")

        self.__rows[index] = Vector(component)

    # 3. b) Умножение на скаляр
    def __imul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Тип {scalar} должен быть int иди float")

        for element in self:
            element *= scalar

        return self

    # Сравнение размерностей двух матриц и бросание исключения
    def __raise_exception(self, other):
        rows_quantity_1 = len(self.__rows)
        columns_quantity_1 = len(self.__rows[0])

        rows_quantity_2 = len(other.__rows)
        columns_quantity_2 = len(other.__rows[0])

        if rows_quantity_1 != rows_quantity_2 or columns_quantity_1 != columns_quantity_2:
            raise ValueError(f"Размеры двух матриц: первой матрицы {rows_quantity_1}x{columns_quantity_1} и "
                             f"второй - {rows_quantity_2}x{columns_quantity_2}, не равны")

    # 3. c) Прибавление к матрице другой матрицы:
    def __iadd__(self, other):
        self.__raise_exception(other)

        rows_quantity_1 = len(self.__rows)

        for i in range(rows_quantity_1):
            self.__rows[i] += other.__rows[i]

        return self

    # 3. d) Вычитание из матрицы другой матрицы:
    def __isub__(self, other):
        self.__raise_exception(other)

        rows_quantity_1 = len(self.__rows)

        for i in range(rows_quantity_1):
            self.__rows[i] -= other.__rows[i]

        return self

    # 3. e) Прибавление к матрице другой матрицы:
    def __add__(self, other):
        self.__raise_exception(other)

        summary = copy.deepcopy(self)
        Matrix.__iadd__(summary, other)
        return summary

    # 3. f) Вычитание матриц:
    def __sub__(self, other):
        self.__raise_exception(other)

        subtraction = copy.deepcopy(self)
        Matrix.__isub__(subtraction, other)
        return subtraction

    # 3. g) Умножение матриц:
    def __mul__(self, other):
        rows_quantity_1 = len(self.__rows)
        rows_quantity_2 = len(other.__rows)
        columns_quantity_1 = len(self.__rows[0])
        columns_quantity_2 = len(other.__rows[0])

        # Проверка размеров матриц в соответствии с правилами умножения матриц
        if columns_quantity_1 != rows_quantity_2:
            raise ValueError(f"Количество строк первой матрицы {rows_quantity_1}x{columns_quantity_1} должно "
                             f"быть равно количеству столбцов второй - {rows_quantity_2}x{columns_quantity_2}")

        multiplication_product = [0] * rows_quantity_1

        for i in range(rows_quantity_1):
            multiplication_product[i] = [0] * columns_quantity_2

        for i in range(rows_quantity_1):
            for j in range(columns_quantity_2):
                for k in range(rows_quantity_2):
                    multiplication_product[i][j] += self.__rows[i][k] * other.__rows[k][j]

        return Matrix(multiplication_product)

    # 3. h) Умножение матрицы на вектор-столбец:
    def multiply_by_vector(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError(f"Объект {vector} не является объектом класса Vector")

        rows_quantity = len(self.__rows)
        columns_quantity = len(self.__rows[0])

        vector_length = len(vector)

        if vector_length != columns_quantity:
            raise ValueError(f"Длина вектора {vector}: {vector_length}, должна "
                             f"быть равна количеству столбцов матрицы - {self}: {columns_quantity}")

        resulted_vector = []

        for i in range(rows_quantity):
            resulted_vector.append(0)

        for i in range(rows_quantity):
            for j in range(columns_quantity):
                resulted_vector[i] += self.__rows[i][j] * vector[j]

        return Vector(resulted_vector)

    # 3. i) Переопределить методы __eq__ и __hash__:
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        self.__raise_exception(other)

        if other.__rows.__hash__ != self.__rows.__hash__:
            return False

        rows_quantity_1 = len(self.__rows)
        rows_quantity_2 = len(other.__rows)

        columns_quantity_1 = len(self.__rows[0])
        columns_quantity_2 = len(other.__rows[0])

        if rows_quantity_1 != rows_quantity_2 or columns_quantity_1 != columns_quantity_2:
            return False
        else:
            for i in range(rows_quantity_1):
                for j in range(columns_quantity_1):
                    if self.__rows[i][j] != other.__rows[i][j]:
                        return False

            return True

    def __hash__(self):
        return hash(tuple(self.__rows))

    # 4. d) Метод __repr__ определить, чтобы результат был в виде: {{1, 2}, {2, 3}}
    def __repr__(self):
        rows_quantity = len(self.__rows)
        strings_lists = ""

        for i in range(rows_quantity):
            strings_lists += (Vector.__repr__(copy.copy(self.__rows[i])))

            if i != rows_quantity - 1:
                strings_lists += ", "

        return "{" + f"{strings_lists}" + "}"

    # 4. b) Транспонирование матрицы:
    def transpose(self):
        rows_quantity = len(self.__rows)
        columns_quantity = len(self.__rows[0])

        multiplication_matrix = []

        for i in range(columns_quantity):
            multiplication_matrix.append(rows_quantity * [0])

        for i in range(rows_quantity):
            for j in range(columns_quantity):
                multiplication_matrix[j][i] = self.__rows[i][j]

        self.__rows = Matrix(multiplication_matrix)

    # Вычисление определителя матриц 1х1 и 2х2
    def get_determinant_of_small_matrix(self, columns_quantity):
        if columns_quantity == 1:
            return self.__rows[0][0]

        if columns_quantity == 2:
            return self.__rows[0][0] * self.__rows[1][1] - self.__rows[1][0] * self.__rows[0][1]

    # 4. c) Вычисление определителя матрицы:
    def get_determinant(self):
        rows_quantity = len(self.__rows)
        columns_quantity = len(self.__rows[0])

        if columns_quantity != rows_quantity:
            raise IndexError(f"Количество строк матрицы должно быть равно количеству столбцов. "
                             f"Сейчас размеры матрицы: {rows_quantity}x{columns_quantity}")

        self.get_determinant_of_small_matrix(columns_quantity)

        def get_inner_determinant(matrix):
            size = len(matrix[0])

            if size == 1:
                return matrix[0][0]

            if size == 2:
                return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

            if size > 2:
                determinant = 0

                for k in range(size):
                    minor = []

                    for i in range(size - 1):
                        minor.append((size - 1) * [0])

                    for i in range(1, size):
                        for j in range(0, k):
                            minor[i - 1][j] = matrix[i][j]

                        for j in range(k + 1, size):
                            minor[i - 1][j - 1] = matrix[i][j]

                    determinant += pow(-1, k) * matrix[0][k] * get_inner_determinant(minor)

                return determinant

        return get_inner_determinant(self.__rows)
