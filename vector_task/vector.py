import math
from multipledispatch import dispatch


class Vector:
    # 1. а) размерность - dimension, все компоненты равны нулю
    @dispatch(int)
    def __init__(self, dimension):
        if not isinstance(dimension, int):
            raise TypeError(f"Тип {dimension} не является int")

        if dimension <= 0:
            raise ValueError(f"Размерность вектора должна быть > 0, но передана размерность {dimension}")

        self.__components = dimension * [0]

    # 1. b) конструктор копирования
    @dispatch(object)
    def __init__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError(f"Объект {vector} не является объектом класса Vector")

        dimension = len(vector)

        self.__components = dimension * [0]

        for i in range(dimension):
            self.__components[i] = vector[i]

    # 1. с) заполнение вектора значениями из списка чисел
    @dispatch(list)
    def __init__(self, components):
        if not isinstance(components, list):
            raise TypeError(f"Объект {components} не является списком")

        if len(components) <= 0:
            raise ValueError(f"Размерность вектора должна быть > 0, но передан список с размерностью {len(components)}")

        for component in components:
            if not isinstance(component, (int, float)):
                raise TypeError(f"Тип всех элементов списка {components} должен быть int или float")

        dimension = len(components)
        self.__components = dimension * [None]

        for i in range(dimension):
            self.__components[i] = components[i]

    # 1. d) заполнение вектора значениями из списка чисел.
    # Если длина списка меньше dimension, то считать, что в остальных компонентах 0.
    @dispatch(int, list)
    def __init__(self, dimension, components):
        if not isinstance(components, list):
            raise TypeError(f"{components} не является списком")

        components_dimension = len(components)

        for component in components:
            if not isinstance(component, (int, float)):
                raise TypeError(f"Элементы списка {components} являются не только числами")

        if not isinstance(dimension, int):
            raise TypeError(f"Тип {dimension} не является int")

        if dimension <= 0:
            raise ValueError(f"Размерность вектора должна быть > 0, но задана размерность - {dimension}")

        self.__components = dimension * [0]

        range_boundary = min(components_dimension, dimension)

        for i in range(range_boundary):
            self.__components[i] = components[i]

    def __len__(self):
        return len(self.__components)

    # 2. Свойства для получения размерности вектора и длины вектора
    @property
    def dimension(self):
        return self.__len__()

    def get_length(self):
        squared_components_sum = 0

        for component in self.__components:
            squared_components_sum += component * component

        return math.sqrt(squared_components_sum)

    # 3. Реализовать метод __repr__, чтобы выдавал информацию о векторе в формате (значения компонент через запятую)
    # Например, {1, 2, 3}
    def __repr__(self):
        strings_list = map(str, self.__components)

        return "{" + ", ".join(strings_list) + "}"

    # g. Переопределить метод __eq__, чтобы было True - векторы имеют одинаковую размерность и соответствующие
    # компоненты равны
    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"Объект {other} не является объектом класса Vector")

        return self.__components == other.__components

    def __hash__(self):
        return hash(tuple(self.__components))

    # 4. Реализовать операторы:
    # a. Прибавление к вектору другого вектора
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"Объект {other} не является объектом класса Vector")

        if self.dimension < other.dimension:
            dimensions_difference = other.dimension - self.dimension

            for i in range(dimensions_difference):
                self.__components.append(0)

        for i in range(other.dimension):
            self.__components[i] += other.__components[i]

        return self

    # b. Вычитание из вектора другого вектора
    def __isub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"Объект {other} не является объектом класса Vector")

        if self.dimension < other.dimension:
            dimensions_difference = other.dimension - self.dimension

            for i in range(dimensions_difference):
                self.__components.append(0)

        for i in range(other.dimension):
            self.__components[i] -= other.__components[i]

        return self

    # с. Сложение двух векторов - должен создаваться новый вектор
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"Объект {other} не является объектом класса Vector")

        sum_vector = Vector(self)
        sum_vector += other

        return sum_vector

    # d. Вычитание векторов - должен создаваться новый вектор
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"Объект {other} не является объектом класса Vector")

        difference_vector = Vector(self)
        difference_vector -= other

        return difference_vector

        # e. Умножение вектора на скаляр
    def __imul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"{scalar} не является числом")

        for i in range(self.dimension):
            self.__components[i] *= scalar

        return self

    # f. Получение и установка компоненты вектора по индексу
    def __getitem__(self, subscript):
        if isinstance(subscript, slice):
            slice_list = []

            start = subscript.start
            stop = subscript.stop
            step = subscript.step

            if step is None:
                step = 1

            if step == 0:
                raise ValueError(f"Индекс step: {step}, не должен быть равен 0")

            if start is None and stop is None:
                if step < 0:
                    start = -self.dimension - 1
                    stop = - 1
                else:
                    start = 0
                    stop = self.dimension

            if stop is None:
                if step < 0:
                    if start <= - 1:
                        stop = - 1
                    else:
                        stop = self.dimension - 1
                else:
                    if start >= 0:
                        stop = self.dimension
                    else:
                        stop = - 1

            if start is None:
                if step < 0:
                    if stop < 0:
                        start = -self.dimension - 1
                    else:
                        start = -1
                else:
                    if stop >= 0:
                        start = 0
                    else:
                        start = -self.dimension

            if not isinstance(start, int):
                raise TypeError(f"Индекс start {start} не является int")

            if not isinstance(stop, int):
                raise TypeError(f"Индекс stop {stop} не является int")

            if not isinstance(step, int):
                raise TypeError(f"Индекс step {step} не является int")

            if step > 0:
                if start < -self.dimension or start >= self.dimension:
                    raise IndexError(
                        f"Индекс start должен быть в диапазоне от -{self.dimension} до {self.dimension - 1}. "
                        f"Переданный индекс start: {start}")

                if stop < -self.dimension + 1 or stop >= self.dimension + 1:
                    raise IndexError(
                        f"Индекс stop должен быть в диапазоне от -{self.dimension - 1} до {self.dimension}. "
                        f"Переданный индекс stop: {stop}")

                if stop > start and ((start >= 0 and stop > 0) or (start < 0 and stop <= 0)):
                    for i in range(start, stop, step):
                        slice_list.append(self.__components[i])

                else:
                    raise IndexError(f"Индекс start: {start}, должен быть < индекса stop: {stop}. "
                                     f"Или индексы должны быть одного знака")

            else:
                if start < -self.dimension - 1 or start > self.dimension - 1:
                    raise IndexError(
                        f"Индекс start должен быть в диапазоне от -{self.dimension + 1} до {self.dimension - 2}. "
                        f"Переданный индекс start: {start}")

                if stop <= -self.dimension or stop >= self.dimension:
                    raise IndexError(
                        f"Индекс stop должен быть в диапазоне от -{self.dimension - 1} до {self.dimension - 1}. "
                        f"Сейчас передан индекс stop: {stop}")

                if stop > start and ((start < 0 and stop < 0) or (start >= -1 and stop > 0)):
                    for i in range(stop, start, step):
                        slice_list.append(self.__components[i])

                else:
                    raise IndexError(f"Индекс start: {start}, должен быть < индекса stop: {stop}. "
                                     f"Или индексы должны быть одного знака")

            return Vector(slice_list)

        else:
            if not isinstance(subscript, int):
                raise TypeError(f"{subscript} не является int")

            if subscript < -self.dimension or subscript >= self.dimension:
                raise IndexError(f"Индекс должен быть в диапазоне от -{self.dimension} до {self.dimension - 1}. "
                                 f"Переданный индекс: {subscript}")

            return self.__components[subscript]

    def __setitem__(self, index, component):
        if not isinstance(index, int):
            raise TypeError(f"{index} не является int")

        if index < - self.dimension or index >= self.dimension:
            raise IndexError(f"Индекс должен быть в диапазоне от -{self.dimension} до {self.dimension - 1}."
                             f"Переданный индекс: {index}")

        self.__components[index] = component

    # Нестатический метод: разворот вектора
    def reverse(self):
        return Vector.__imul__(self, -1)

    @staticmethod
    def get_scalar_product(vector_1, vector_2):
        if not isinstance(vector_1, Vector):
            raise TypeError(f"Объект {vector_1} не является объектом класса Vector")

        if not isinstance(vector_2, Vector):
            raise TypeError(f"Объект {vector_2} не является объектом класса Vector")

        min_dimension = min(vector_1.dimension, vector_2.dimension)

        scalar_product = 0

        for i in range(min_dimension):
            scalar_product += vector_1[i] * vector_2[i]

        return scalar_product
