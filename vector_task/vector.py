import math
from multipledispatch import dispatch


class Vector:
    # 1. а) размерность - dimension, все компоненты равны нулю
    @dispatch(int)
    def __init__(self, dimension):
        if not isinstance(dimension, int):
            raise TypeError(f"Тип dimension: {dimension}, не является int. "
                            f"Сейчас тип dimension: {type(dimension).__name__}")

        if dimension <= 0:
            raise ValueError(f"Размерность вектора dimension должна быть > 0, но передана размерность {dimension}")

        self.__components = dimension * [0]

    # 1. b) конструктор копирования
    @dispatch(object)
    def __init__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError(f"Объект vector: {vector}, не является объектом класса Vector. "
                            f"Сейчас тип vector: {type(vector).__name__}")

        dimension = len(vector)

        vector_list = dimension * [0]

        for i in range(dimension):
            vector_list[i] = vector[i]

        self.__components = vector_list.copy()

    # 1. с) заполнение вектора значениями из списка чисел
    @dispatch(list)
    def __init__(self, components):
        if not isinstance(components, list):
            raise TypeError(f"Объект components: {components}, не является списком. "
                            f"Сейчас тип components: {type(components).__name__}")

        if len(components) <= 0:
            raise ValueError("Размерность вектора должна быть > 0, но передан список "
                             f"components с размерностью {len(components)}")

        for component in components:
            if not isinstance(component, (int, float)):
                raise TypeError(f"Тип всех элементов списка components: {components}, должен быть int или float. "
                                f"Сейчас тип component: {type(component).__name__}")

        self.__components = components.copy()

    # 1. d) заполнение вектора значениями из списка чисел.
    # Если длина списка меньше dimension, то считать, что в остальных компонентах 0.
    @dispatch(int, list)
    def __init__(self, dimension, components):
        if not isinstance(components, list):
            raise TypeError(f"Переменная components: {components}, не является списком. "
                            f"Сейчас тип components: {type(components).__name__}")

        components_dimension = len(components)

        for component in components:
            if not isinstance(component, (int, float)):
                raise TypeError(f"Элементы списка components: {components}, являются не только числами. "
                                f"Сейчас тип component: {type(component).__name__}")

        if not isinstance(dimension, int):
            raise TypeError(f"Тип dimension: {dimension}, не является int. "
                            f"Сейчас тип dimension: {type(dimension).__name__}")

        if dimension <= 0:
            raise ValueError(f"Размерность вектора dimension должна быть > 0, но задана размерность - {dimension}")

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
            raise TypeError(f"Объект other: {other}, не является объектом класса Vector. "
                            f"Сейчас тип other: {type(other).__name__}")

        return self.__components == other.__components

    def __hash__(self):
        return hash(tuple(self.__components))

    # 4. Реализовать операторы:
    # a. Прибавление к вектору другого вектора
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"Объект other: {other}, не является объектом класса Vector. "
                            f"Сейчас тип other: {type(other).__name__}")

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
            raise TypeError(f"Объект other: {other}, не является объектом класса Vector. "
                            f"Сейчас тип other: {type(other).__name__}")

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
            raise TypeError(f"Объект other: {other}, не является объектом класса Vector. "
                            f"Сейчас тип other: {type(other).__name__}")

        sum_vector = Vector(self)
        sum_vector += other

        return sum_vector

    # d. Вычитание векторов - должен создаваться новый вектор
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"Объект other: {other}, не является объектом класса Vector. "
                            f"Сейчас тип other: {type(other).__name__}")

        difference_vector = Vector(self)
        difference_vector -= other

        return difference_vector

        # e. Умножение вектора на скаляр

    def __imul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Переменная scalar: {scalar}, не является числом. "
                            f"Сейчас тип scalar: {type(scalar).__name__}")

        for i in range(self.dimension):
            self.__components[i] *= scalar

        return self

    # f. Получение и установка компоненты вектора по индексу
    def __getitem__(self, key):
        if isinstance(key, slice):
            user_list = []

            for i in range(self.dimension):
                user_list.append(self.__components[i])

            slice_list = user_list[key.start:key.stop:key.step]

            if len(slice_list) == 0:
                return None

            return Vector(slice_list)

        if not isinstance(key, int):
            raise TypeError(f"Индекс key: {key}, не является int. "
                            f"Сейчас тип key: {type(key).__name__}")

        if key < -self.dimension or key >= self.dimension:
            raise IndexError(f"Индекс key должен быть в диапазоне от -{self.dimension} до {self.dimension - 1}. "
                             f"Переданный индекс key: {key}")

        return self.__components[key]

    def __setitem__(self, index, component):
        if not isinstance(index, int):
            raise TypeError(f"Индекс index: {index}, не является int. "
                            f"Сейчас тип index: {type(index).__name__}")

        if index < -self.dimension or index >= self.dimension:
            raise IndexError(f"Индекс index должен быть в диапазоне от -{self.dimension} до {self.dimension - 1}."
                             f"Переданный индекс index: {index}")

        self.__components[index] = component

    # Нестатический метод: разворот вектора
    def reverse(self):
        return Vector.__imul__(self, -1)

    @staticmethod
    def get_scalar_product(vector_1, vector_2):
        if not isinstance(vector_1, Vector):
            raise TypeError(f"Объект vector_1: {vector_1}, не является объектом класса Vector. "
                            f"Сейчас тип vector_1: {type(vector_1).__name__}")

        if not isinstance(vector_2, Vector):
            raise TypeError(f"Объект vector_2: {vector_2}, не является объектом класса Vector. "
                            f"Сейчас тип vector_2: {type(vector_2).__name__}")

        min_dimension = min(vector_1.dimension, vector_2.dimension)

        scalar_product = 0

        for i in range(min_dimension):
            scalar_product += vector_1[i] * vector_2[i]

        return scalar_product
