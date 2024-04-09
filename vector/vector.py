import math
from multipledispatch import dispatch
import copy


class Vector:
    # 1. а) размерность n, все компонены равны нулю
    @dispatch(int)
    def __init__(self, n):
        if n <= 0:
            raise ValueError

        if isinstance(n, int):
            self.__n = n
            self.__vector = n * [0]

    # 1. b) конструктор копирования
    @dispatch((list, object))
    def __init__(self, vector):
        self.__vector = copy.deepcopy(vector)

    # 1. с) заполнение вектора значениями из списка чисел
    @dispatch((list, float))
    def __init__(self, components):
        self.__vector = []

        for i, number in enumerate(components):
            number = components[i]

            self.__vector.append(number)

    # 1. d) заполнение вектора значениями из списка чисел.
    # Если длина списка меньше n, то считать, что в остальных компонентах 0.
    @dispatch(int, (list, object))
    def __init__(self, n, components):
        if n <= 0:
            raise ValueError

        length = len(components)

        if length > n:
            raise ValueError

        while length < n:
            components.append(0)
            length += 1

        self.__vector = components

    # 2. Свойства для получения размерности вектора и длины вектора
    @property
    def vector_dimension(self):
        return len(self.__vector)

    @property
    def vector_length(self):
        current_vector_length = 0
        for e in self.__vector:
            current_vector_length += e * e

        return math.sqrt(current_vector_length)

    # 3. Реализовать метод __repr__, чтобы выдавал информацию о векторе в формате (значения компонент через запятую)
    # Например, {1, 2, 3}
    def __repr__(self):
        list_length = len(self.__vector)

        numbers_string = "{"

        for i, number in enumerate(self.__vector):
            numbers_string += str(number)

            if i != list_length - 1:
                numbers_string += ", "

        numbers_string += "}"

        return f"{numbers_string}"

    # g. Переопределить метод __eq__, чтобы было True - векторы имеют одинаковую размерность и соответствующие
    # компоненты равны
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return len(self.__vector) == len(other.__vector) and self.__vector == other.__vector

    def __hash__(self):
        return hash((self.__n, self.__vector))

    # 4. Реализовать операторы:
    # a. Прибавление к вектору другого вектора
    def get_sum_vector(self, other):
        vector_1_length = len(self.__vector)
        vector_2_length = len(other.__vector)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector.append(0)

        for i, number_1 in enumerate(self.__vector):
            number_1 = self.__vector[i]

            for j, number_2 in enumerate(other.__vector):
                if i == j:
                    number_2 = other.__vector[i]
                    number_1 += number_2
                    self.__vector[i] = number_1

        return self.__vector

    # b. Вычитание из вектора другого вектора
    def get_diff_vector(self, other):
        vector_1_length = len(self.__vector)
        vector_2_length = len(other.__vector)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector.append(0)

        for i, number_1 in enumerate(self.__vector):
            number_1 = self.__vector[i]

            for j, number_2 in enumerate(other.__vector):
                if i == j:
                    number_2 = other.__vector[i]
                    self.__vector[i] = number_1 - number_2

        return self.__vector

    # с. Сложение двух векторов - должен создаваться новый вектор
    def get_sum_new_vector(self, other):
        vector_1_length = len(self.__vector)
        vector_2_length = len(other.__vector)

        max_length = vector_1_length if vector_1_length > vector_2_length else vector_2_length

        sum_vector = []
        for i in range(max_length):
            sum_vector.append(0)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector.append(0)

        for i, sum_number in enumerate(sum_vector):

            for j, number_1 in enumerate(self.__vector):
                number_1 = self.__vector[j]

                for k, number_2 in enumerate(other.__vector):
                    number_2 = other.__vector[k]

                    if i == j and j == k:
                        sum_vector[k] = number_1 + number_2

        return sum_vector

    # d. Вычитание векторов - должен создаваться новый вектор
    def get_difference_new_vector(self, other):
        vector_1_length = len(self.__vector)
        vector_2_length = len(other.__vector)

        max_length = vector_1_length if vector_1_length > vector_2_length else vector_2_length

        difference_vector = []
        for i in range(max_length):
            difference_vector.append(0)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector.append(0)

        for i, sum_number in enumerate(difference_vector):

            for j, number_1 in enumerate(self.__vector):
                number_1 = self.__vector[j]

                for k, number_2 in enumerate(other.__vector):
                    number_2 = other.__vector[k]

                    if i == j and j == k:
                        difference_vector[k] = number_1 - number_2

        return difference_vector

        # e. Умножение вектора на скаляр

    def get_multiplied_vector(self, scalar):
        for i, item in enumerate(self.__vector):
            self.__vector[i] *= scalar

        return self.__vector

    # f. Получение и установка компоненты вектора по индексу
    def get_vector_component(self, index):
        if index >= len(self.__vector) or index < 0:
            raise ValueError

        for i, item in enumerate(self.__vector):
            if i == index:
                return item

    def change_vector_component(self, index, number):
        if index >= len(self.__vector) or index < 0:
            raise ValueError

        for i, item in enumerate(self.__vector):
            if i == index:
                self.__vector[i] = number

        return self.__vector

    # Нестатический метод: разворот вектора
    def get_reverse_vector(self):
        for i, number in enumerate(self.__vector):
            self.__vector[i] = (- 1) * number

        return self.__vector

    def scalar_multiplicate_vectors(self, other):
        vector_1_length = len(self.__vector)
        vector_2_length = len(other.__vector)

        if vector_1_length > vector_2_length:
            length_difference = vector_1_length - vector_2_length

            for i in range(length_difference):
                other.__vector.append(0)
        else:
            length_difference = vector_2_length - vector_1_length

            for i in range(length_difference):
                self.__vector.append(0)

        for i, number_1 in enumerate(self.__vector):
            self.__vector[i] = number_1
            for j, number_2 in enumerate(other.__vector):
                number_2 = other.__vector[j]
                if i == j:
                    self.__vector[i] *= number_2

        return self.__vector
