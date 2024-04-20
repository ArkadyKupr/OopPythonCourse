import math
from multipledispatch import dispatch
import copy


class Vector:
    # 1. а) размерность n, все компонены равны нулю
    @dispatch(int)
    def __init__(self, n):
        if n <= 0:
            raise ValueError(f"Длина вектора {n} меньше или равна нулю")

        if not isinstance(n, int):
            raise TypeError(f"Тип {n} не является int")

        self.__vector_components = n * [0]
        self.__vector_length = n

    # 1. b) конструктор копирования
    @dispatch(object)
    def __init__(self, vector):
        if not isinstance(vector, list):
            raise TypeError(f"Объект {vector} не является списком")

        vector_length = len(vector)
        self.__vector_length = vector_length
        self.__vector_components = []

        for i in range(vector_length):
            self.__vector_components.append(copy.deepcopy(vector[i]))

    # 1. с) заполнение вектора значениями из списка чисел
    @dispatch(list)
    def __init__(self, components):
        if not isinstance(components, list):
            raise TypeError(f"Объект {components} не является списком")

        self.__vector_components = copy.deepcopy(components)
        self.__vector_length = len(components)

    # 1. d) заполнение вектора значениями из списка чисел.
    # Если длина списка меньше n, то считать, что в остальных компонентах 0.
    @dispatch(int, list)
    def __init__(self, n, components):
        if n <= 0:
            raise ValueError(f"Длина вектора {n} меньше или равна нулю")

        if not isinstance(components, list):
            raise TypeError(f"{components} не является списком")

        if not isinstance(n, int):
            raise TypeError(f"Тип {n} не является int")

        self.__vector_components = n * [0]
        self.__vector_length = n

        components_length = len(components)

        for i in range(components_length):
            self.__vector_components[i] = copy.deepcopy(components[i])

    # 2. Свойства для получения размерности вектора и длины вектора
    @property
    def dimension(self):
        return self.__vector_length

    def get_length(self):
        squared_components_sum = 0

        for component in self.__vector_components:
            squared_components_sum += component * component

        return math.sqrt(squared_components_sum)

    # 3. Реализовать метод __repr__, чтобы выдавал информацию о векторе в формате (значения компонент через запятую)
    # Например, {1, 2, 3}
    def __repr__(self):
        vector = []

        for i, number in enumerate(self.__vector_components):
            vector.append(str(number))

        return "{" + ", ".join(vector) + "}"

    # g. Переопределить метод __eq__, чтобы было True - векторы имеют одинаковую размерность и соответствующие
    # компоненты равны
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__vector_components == other.__vector_components

    def __hash__(self):
        return hash(tuple(self.__vector_components))

    # 4. Реализовать операторы:
    # a. Прибавление к вектору другого вектора
    def __iadd__(self, other):
        if not isinstance(self.__vector_components, list):
            raise TypeError(f"{self.__vector_components} не является вектором")

        if not isinstance(other.__vector_components, list):
            raise TypeError(f"{self.__vector_components} не является вектором")

        vector_1_length = len(self.__vector_components)
        vector_2_length = len(other.__vector_components)

        if vector_1_length > vector_2_length:
            for i in range(vector_2_length):
                self.__vector_components[i] += other.__vector_components[i]

        else:
            lengths_difference = vector_2_length - vector_1_length

            for i in range(lengths_difference):
                self.__vector_components.append(0)

            for i in range(vector_2_length):
                self.__vector_components[i] += other.__vector_components[i]

        return self

    # b. Вычитание из вектора другого вектора
    def __isub__(self, other):
        if not isinstance(self.__vector_components, list):
            raise TypeError(f"{self.__vector_components} не является вектором")

        if not isinstance(other.__vector_components, list):
            raise TypeError(f"{self.__vector_components} не является вектором")

        vector_1_length = len(self.__vector_components)
        vector_2_length = len(other.__vector_components)

        if vector_1_length > vector_2_length:
            for i in range(vector_2_length):
                self.__vector_components[i] -= other.__vector_components[i]

        else:
            lengths_difference = vector_2_length - vector_1_length

            for i in range(lengths_difference):
                self.__vector_components.append(0)

            for i in range(vector_2_length):
                self.__vector_components[i] -= other.__vector_components[i]

        return self

    # с. Сложение двух векторов - должен создаваться новый вектор
    def __add__(self, other):
        if not isinstance(self.__vector_components, list):
            raise TypeError(f"{self.__vector_components} не является вектором")

        if not isinstance(other.__vector_components, list):
            raise TypeError(f"{self.__vector_components} не является вектором")

        vector_1_length = len(self.__vector_components)
        vector_2_length = len(other.__vector_components)

        sum_vector = []

        if vector_1_length > vector_2_length:
            for i in range(vector_1_length):
                sum_vector.append(0)

            for i in range(vector_2_length):
                sum_vector[i] = self.__vector_components[i] + other.__vector_components[i]

            for i in range(vector_2_length, vector_1_length):
                sum_vector[i] = self.__vector_components[i]

        else:
            for i in range(vector_2_length):
                sum_vector.append(0)

            for i in range(vector_1_length):
                sum_vector[i] = self.__vector_components[i] + other.__vector_components[i]

            for i in range(vector_1_length, vector_2_length):
                sum_vector[i] = other.__vector_components[i]

        return sum_vector

    # d. Вычитание векторов - должен создаваться новый вектор
    def __sub__(self, other):
        if not isinstance(self.__vector_components, list):
            raise TypeError(f"{self.__vector_components} не является вектором")

        if not isinstance(other.__vector_components, list):
            raise TypeError(f"{self.__vector_components} не является вектором")

        vector_1_length = len(self.__vector_components)
        vector_2_length = len(other.__vector_components)

        difference_vector = []

        if vector_1_length > vector_2_length:
            for i in range(vector_1_length):
                difference_vector.append(0)

            for i in range(vector_2_length):
                difference_vector[i] = self.__vector_components[i] - other.__vector_components[i]

            for i in range(vector_2_length, vector_1_length):
                difference_vector[i] = self.__vector_components[i]

        else:
            for i in range(vector_2_length):
                difference_vector.append(0)

            for i in range(vector_1_length):
                difference_vector[i] = self.__vector_components[i] - other.__vector_components[i]

            for i in range(vector_1_length, vector_2_length):
                difference_vector[i] = other.__vector_components[i]

        return difference_vector

        # e. Умножение вектора на скаляр
    def __imul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"{scalar} не является числом")

        vector_length = len(self.__vector_components)

        for i in range(vector_length):
            self.__vector_components[i] *= scalar

        return self

    # f. Получение и установка компоненты вектора по индексу
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"{index} не является int")

        vector_length = len(self.__vector_components)

        if index < 0 or index >= vector_length:
            raise IndexError(f"Индекс {index} больше или равен длине вектора - {vector_length}")

        return self.__vector_components[index]

    def __setitem__(self, index, component):
        if not isinstance(index, int):
            raise TypeError(f"{index} не является int")

        if not isinstance(component, (int, float)):
            raise TypeError(f"{component} не является числом")

        vector_length = len(self.__vector_components)

        if index < 0 or index >= vector_length:
            raise IndexError(f"Индекс {index} больше или равен длине вектора - {vector_length}")

        self.__vector_components[index] = component

        return self.__vector_components

    # Нестатический метод: разворот вектора
    def reverse_vector(self):
        vector_length = len(self.__vector_components)

        for i in range(vector_length):
            self.__vector_components[i] *= -1

        return self

    def __len__(self):
        return len(self.__vector_components)

    @staticmethod
    def get_scalar_multiplication(vector_1, vector_2):
        vector_1_length = len(vector_1)
        vector_2_length = len(vector_2)

        max_length = vector_1_length if vector_1_length > vector_2_length else vector_2_length
        min_length = vector_1_length if vector_1_length <= vector_2_length else vector_2_length

        multiplied_vector = []

        for i in range(min_length):
            multiplied_vector.append(vector_1[i] * vector_2[i])

        for i in range(min_length, max_length):
            multiplied_vector.append(0)

        return multiplied_vector
