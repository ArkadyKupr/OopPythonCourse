import math
from multipledispatch import dispatch
import copy


class Vector:
    # 1. а) размерность - dimension, все компоненты равны нулю
    @dispatch(int)
    def __init__(self, dimension):
        if not isinstance(dimension, int):
            raise TypeError(f"Тип {dimension} не является int")

        if dimension <= 0:
            raise ValueError(f"Размерность вектора должна быть больше нуля, но передана размерность {dimension}")

        self.__components = dimension * [0]

    # 1. b) конструктор копирования
    @dispatch(object)
    def __init__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError(f"Объект {vector} не является объектом класса Vector")

        self.__components = copy.copy(vector)

    # 1. с) заполнение вектора значениями из списка чисел
    @dispatch(list)
    def __init__(self, components):
        if not isinstance(components, list):
            raise TypeError(f"Объект {components} не является списком")

        components_dimension = len(components)

        for i in range(components_dimension):
            if not isinstance(components[i], (int, float)):
                raise TypeError(f"Элементы списка {components} являются не только числами")

        self.__components = copy.copy(components)

    # 1. d) заполнение вектора значениями из списка чисел.
    # Если длина списка меньше dimension, то считать, что в остальных компонентах 0.
    @dispatch(int, list)
    def __init__(self, dimension, components):
        if not isinstance(components, list):
            raise TypeError(f"{components} не является списком")

        components_dimension = len(components)

        for i in range(components_dimension):
            if not isinstance(components[i], (int, float)):
                raise TypeError(f"Элементы списка {components} являются не только числами")

        if not isinstance(dimension, int):
            raise TypeError(f"Тип {dimension} не является int")

        if components_dimension < dimension:
            self.__components = dimension * [0]

            for i in range(components_dimension):
                self.__components[i] = copy.copy(components[i])

        else:
            self.__components = components_dimension * [0]

            for i in range(components_dimension):
                self.__components[i] = copy.copy(components[i])

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
    @staticmethod
    def copy(component):
        return str(copy.copy(component))

    def __repr__(self):
        strings_list = map(self.copy, self.__components)

        return "{" + ", ".join(strings_list) + "}"

    # g. Переопределить метод __eq__, чтобы было True - векторы имеют одинаковую размерность и соответствующие
    # компоненты равны
    def __eq__(self, other):
        return self.__components == other.__components

    def __hash__(self):
        return hash(tuple(self.__components))

    # 4. Реализовать операторы:
    # a. Прибавление к вектору другого вектора
    def __iadd__(self, other):
        vector_1_dimension = len(self.__components)
        vector_2_dimension = len(other.__components)

        if vector_1_dimension <= vector_2_dimension:
            dimensions_difference = vector_2_dimension - vector_1_dimension

            for i in range(dimensions_difference):
                self.__components.append(0)

        for i in range(vector_1_dimension):
            self.__components[i] += other.__components[i]

        return self

    # b. Вычитание из вектора другого вектора
    def __isub__(self, other):
        vector_1_dimension = len(self.__components)
        vector_2_dimension = len(other.__components)

        if vector_1_dimension <= vector_2_dimension:
            dimensions_difference = vector_2_dimension - vector_1_dimension

            for i in range(dimensions_difference):
                self.__components.append(0)

        for i in range(vector_1_dimension):
            self.__components[i] -= other.__components[i]

        return self

    # с. Сложение двух векторов - должен создаваться новый вектор
    def __add__(self, other):
        sum_vector = copy.deepcopy(self)
        Vector.__iadd__(sum_vector, other)
        return sum_vector

    # d. Вычитание векторов - должен создаваться новый вектор
    def __sub__(self, other):
        difference_vector = copy.deepcopy(self)
        Vector.__isub__(difference_vector, other)
        return difference_vector

        # e. Умножение вектора на скаляр

    def __imul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"{scalar} не является числом")

        length = len(self.__components)

        for i in range(length):
            self.__components[i] *= scalar

        return self

    # f. Получение и установка компоненты вектора по индексу
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"{index} не является int")

        if index < 0:
            raise IndexError(f"Индекс {index} должен быть равен или больше 0")

        dimension = len(self.__components)

        if index >= dimension:
            raise IndexError(f"Индекс {index} равен или больше размерности вектора - {dimension}")

        return self.__components[slice(index, index + 1)][0]

    def __setitem__(self, index, component):
        if not isinstance(index, int):
            raise TypeError(f"{index} не является int")

        if index < 0:
            raise IndexError(f"Индекс {index} должен быть равен или больше 0")

        dimension = len(self.__components)

        if index >= dimension:
            raise IndexError(f"Индекс {index} равен или больше размерности вектора - {dimension}")

        self.__components[index] = component

    # Нестатический метод: разворот вектора
    def reverse_vector(self):
        return Vector.__imul__(self, -1)

    @staticmethod
    def get_scalar_product(vector_1, vector_2):
        if not isinstance(vector_1, Vector):
            raise TypeError(f"Объект {vector_1} не является объектом класса Vector")

        if not isinstance(vector_2, Vector):
            raise TypeError(f"Объект {vector_2} не является объектом класса Vector")

        vector_1_dimension = len(vector_1)
        vector_2_dimension = len(vector_2)

        min_dimension = min(vector_1_dimension, vector_2_dimension)

        scalar_product = 0

        for i in range(min_dimension):
            scalar_product += vector_1[i] * vector_2[i]

        return scalar_product
