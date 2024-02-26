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

    def __repr__(self):
        list_length = len(self.__vector)

        numbers_string = "{"

        for i, number in enumerate(self.__vector):
            numbers_string += str(number)

            if i != list_length - 1:
                numbers_string += " ,"

        numbers_string += "}"

        return f"{numbers_string}"


user_vector = Vector([1, 2, 3])
print(user_vector)
