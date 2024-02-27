from multipledispatch import dispatch
import copy


class Vector:
    @dispatch(int)
    def __init__(self, n):
        if n <= 0:
            raise ValueError

        if isinstance(n, int):
            self.__n = n
            self.__vector = n * [0]

    @dispatch(int, list)
    def __init__(self, n, components):
        if n <= 0:
            raise ValueError

        if len(components) > n:
            raise ValueError

        length = len(components)

        while length < n:
            components.append(0)
            length += 1

        self.__vector = components

    @dispatch(list)
    def __init__(self, vector):
        self.__vector = vector.copy()

    @dispatch(list)
    def __init__(self, vector):
        self.__vector = copy.copy(vector)

    @property
    def vector_length(self):
        return len(self.__vector)

    def __repr__(self):
        list_length = len(self.__vector)

        numbers_string = "{"

        for i, number in enumerate(self.__vector):
            numbers_string += str(number)

            if i != list_length - 1:
                numbers_string += " ,"

        numbers_string += "}"

        return f"{numbers_string}"


def get_sum_vector(vector_1, vector_2):
    vector_1_length = len(vector_1)
    vector_2_length = len(vector_2)

    if vector_1_length >= vector_2_length:
        for i, value_1 in enumerate(vector_1):
            value_1 = vector_1[i]

            if i < vector_2_length:

                for j, value_2 in enumerate(vector_2):
                    if i == j:
                        value_2 = vector_2[j]
                        value_1 += value_2
                        vector_1[i] = value_1

    else:
        length_difference = vector_2_length - vector_1_length

        for i in range(length_difference):
            vector_1.append(0)

        for i, value_1 in enumerate(vector_1):
            value_1 = vector_1[i]

            for j, value_2 in enumerate(vector_2):
                if i == j:
                    value_1 += vector_2[j]
                    vector_1[i] = value_1

    return vector_1


def get_diff_vector(vector_1, vector_2):
    vector_1_length = len(vector_1)
    vector_2_length = len(vector_2)

    if vector_1_length >= vector_2_length:
        for i, value_1 in enumerate(vector_1):
            value_1 = vector_1[i]

            if i < vector_2_length:

                for j, value_2 in enumerate(vector_2):
                    if i == j:
                        value_2 = vector_2[j]
                        value_1 -= value_2
                        vector_1[i] = value_1

    else:
        length_difference = vector_2_length - vector_1_length

        for i in range(length_difference):
            vector_1.append(0)

        for i, value_1 in enumerate(vector_1):
            value_1 = vector_1[i]

            for j, value_2 in enumerate(vector_2):
                if i == j:
                    value_1 -= vector_2[j]
                    vector_1[i] = value_1

    return vector_1


def get_sum_new_vector(vector_1, vector_2):
    vector_1_length = len(vector_1)
    vector_2_length = len(vector_2)

    max_length = vector_1_length if vector_1_length > vector_2_length else vector_2_length

    sum_vector = []
    for i in range(max_length):
        sum_vector.append(0)

    if vector_1_length > vector_2_length:
        length_difference = vector_1_length - vector_2_length

        for i in range(length_difference):
            vector_2.append(0)
    else:
        length_difference = vector_2_length - vector_1_length

        for i in range(length_difference):
            vector_1.append(0)

    for i, sum_value in enumerate(sum_vector):

        for j, value_1 in enumerate(vector_1):
            value_1 = vector_1[j]

            for k, value_2 in enumerate(vector_2):
                value_2 = vector_2[k]

                if i == j and j == k:
                    sum_vector[i] = value_1 + value_2

    return sum_vector


user_vector = Vector([1, 2, 3])
user_vector_1 = Vector([1, 2, 3])

print(user_vector.vector_length)

print(user_vector)

print(get_sum_new_vector([1, 2, 7, 3, 9], [1, 5, 5, 9, 3, 8]))
