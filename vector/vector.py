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

        return (len(self.__vector_components) == len(other.__vector_components)
                and self.__vector_components == other.__vector_components)

    def __hash__(self):
        return hash((self.__vector_length, self.__vector_components))

    # 4. Реализовать операторы:
    # a. Прибавление к вектору другого вектора
    def get_sum_vector(self, other):
        vector_1_length = len(self.__vector_components)
        vector_2_length = len(other.__vector_components)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector_components.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector_components.append(0)

        for i, number_1 in enumerate(self.__vector_components):
            number_1 = self.__vector_components[i]

            for j, number_2 in enumerate(other.__vector_components):
                if i == j:
                    number_2 = other.__vector_components[i]
                    number_1 += number_2
                    self.__vector_components[i] = number_1

        return self.__vector_components

    # b. Вычитание из вектора другого вектора
    def get_diff_vector(self, other):
        vector_1_length = len(self.__vector_components)
        vector_2_length = len(other.__vector_components)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector_components.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector_components.append(0)

        for i, number_1 in enumerate(self.__vector_components):
            number_1 = self.__vector_components[i]

            for j, number_2 in enumerate(other.__vector_components):
                if i == j:
                    number_2 = other.__vector_components[i]
                    self.__vector_components[i] = number_1 - number_2

        return self.__vector_components

    # с. Сложение двух векторов - должен создаваться новый вектор
    def get_sum_new_vector(self, other):
        vector_1_length = len(self.__vector_components)
        vector_2_length = len(other.__vector_components)

        max_length = vector_1_length if vector_1_length > vector_2_length else vector_2_length

        sum_vector = []
        for i in range(max_length):
            sum_vector.append(0)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector_components.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector_components.append(0)

        for i, sum_number in enumerate(sum_vector):

            for j, number_1 in enumerate(self.__vector_components):
                number_1 = self.__vector_components[j]

                for k, number_2 in enumerate(other.__vector_components):
                    number_2 = other.__vector_components[k]

                    if i == j and j == k:
                        sum_vector[k] = number_1 + number_2

        return sum_vector

    # d. Вычитание векторов - должен создаваться новый вектор
    def get_difference_new_vector(self, other):
        vector_1_length = len(self.__vector_components)
        vector_2_length = len(other.__vector_components)

        max_length = vector_1_length if vector_1_length > vector_2_length else vector_2_length

        difference_vector = []
        for i in range(max_length):
            difference_vector.append(0)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector_components.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector_components.append(0)

        for i, sum_number in enumerate(difference_vector):

            for j, number_1 in enumerate(self.__vector_components):
                number_1 = self.__vector_components[j]

                for k, number_2 in enumerate(other.__vector_components):
                    number_2 = other.__vector_components[k]

                    if i == j and j == k:
                        difference_vector[k] = number_1 - number_2

        return difference_vector

        # e. Умножение вектора на скаляр

    def get_multiplied_vector(self, scalar):
        for i, item in enumerate(self.__vector_components):
            self.__vector_components[i] *= scalar

        return self.__vector_components

    # f. Получение и установка компоненты вектора по индексу
    def get_vector_component(self, index):
        if index >= len(self.__vector_components) or index < 0:
            raise ValueError

        for i, item in enumerate(self.__vector_components):
            if i == index:
                return item

    def change_vector_component(self, index, number):
        if index >= len(self.__vector_components) or index < 0:
            raise ValueError

        for i, item in enumerate(self.__vector_components):
            if i == index:
                self.__vector_components[i] = number

        return self.__vector_components

    # Нестатический метод: разворот вектора
    def get_reverse_vector(self):
        for i, number in enumerate(self.__vector_components):
            self.__vector_components[i] = (- 1) * number

        return self.__vector_components

    def scalar_multiplicate_vectors(self, other):
        vector_1_length = len(self.__vector_components)
        vector_2_length = len(other.__vector_components)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector_components.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector_components.append(0)

        for i, number_1 in enumerate(self.__vector_components):
            self.__vector_components[i] = number_1
            for j, number_2 in enumerate(other.__vector_components):
                number_2 = other.__vector_components[j]
                if i == j:
                    self.__vector_components[i] *= number_2

        return self.__vector_components
