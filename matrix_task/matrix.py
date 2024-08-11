from multipledispatch import dispatch
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
    def __compare_dimensions(self, other):
        if self.rows_quantity != other.rows_quantity or self.columns_quantity != other.columns_quantity:
            raise ValueError(f"Размеры двух матриц: первой матрицы {self.rows_quantity}x{self.columns_quantity} и "
                             f"второй - {other.rows_quantity}x{other.columns_quantity}, не равны")

    # 3. c) Прибавление к матрице другой матрицы:
    def __iadd__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        self.__compare_dimensions(other)

        for i in range(self.rows_quantity):
            self.__rows[i] += other.__rows[i]

        return self

    # 3. d) Вычитание из матрицы другой матрицы:
    def __isub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        self.__compare_dimensions(other)

        for i in range(self.rows_quantity):
            self.__rows[i] -= other.__rows[i]

        return self

    # 3. e) Прибавление к матрице другой матрицы:
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        self.__compare_dimensions(other)

        matrices_sum = Matrix(self.rows_quantity, self.columns_quantity)
        Matrix.__iadd__(matrices_sum, other)
        return matrices_sum

    # 3. f) Вычитание матриц:
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        self.__compare_dimensions(other)

        matrices_difference = Matrix(self.rows_quantity, self.columns_quantity)
        Matrix.__isub__(matrices_difference, other)
        return matrices_difference

    # 3. g) Умножение матриц:
    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Объект {other} не является объектом класса Matrix")

        # Проверка размеров матриц в соответствии с правилами умножения матриц
        if self.columns_quantity != other.rows_quantity:
            raise ValueError(f"Количество столбцов первой матрицы {self.rows_quantity}x{self.columns_quantity} должно "
                             f"быть равно количеству строк второй - {other.rows_quantity}x{other.columns_quantity}")

        product = [None] * self.rows_quantity

        for i in range(self.rows_quantity):
            product[i] = [0] * other.columns_quantity

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

        result_vector = [0] * self.rows_quantity

        for i in range(self.rows_quantity):
            for j in range(self.columns_quantity):
                result_vector[i] += self.__rows[i][j] * vector[j]

        return Vector(result_vector)

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
    def transpose(self):
        result_matrix = []

        for i in range(self.columns_quantity):
            result_matrix.append(self.rows_quantity * [0])

        for i in range(self.rows_quantity):
            for j in range(self.columns_quantity):
                result_matrix[j][i] = self.__rows[i][j]

        return Matrix(result_matrix)

    # 4. c) Вычисление определителя матрицы:
    def get_determinant(self):
        if self.columns_quantity != self.rows_quantity:
            raise ValueError(f"Количество строк матрицы должно быть равно количеству столбцов. "
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
                    for j in range(0, k):
                        minor[i - 1][j] = matrix[i][j]

                    for j in range(k + 1, size):
                        minor[i - 1][j - 1] = matrix[i][j]

                determinant += pow(-1, k) * matrix[0][k] * get_determinant_inner(minor)

            return determinant

        return get_determinant_inner(self.__rows)
