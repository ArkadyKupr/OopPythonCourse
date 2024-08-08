import copy


class ArrayList:
    def __init__(self, capacity=None):
        if capacity is None:
            self.__capacity = 10
        else:
            if not isinstance(capacity, int):
                raise TypeError(f"Тип {capacity} должен быть int")

            if capacity < 0:
                raise ValueError(f"{capacity} должен быть больше нуля")

            self.__capacity = capacity

        self.__items = [None] * self.__capacity
        self.__size = 0

    def __len__(self):
        return self.__size

    def check(self, item):
        if not isinstance(item, int):
            raise TypeError(f"Тип {item} должен быть int")

        if item < 0 or item > self.__size:
            raise ValueError(f"{item} должен лежать в пределе [0, {self.__size}]")

    def __getitem__(self, item):
        self.check(item)

        return self.__items[item]

    def __setitem__(self, key, value):
        self.check(key)

        self.__items[key] = value

        self.__size += 1

    def pop(self, index):
        self.check(index)

        if index < self.__size - 1:
            for i in range(index, self.__size):
                self.__items[i] = self.__items[i + 1]

        self.__items[self.__size - 1] = None
        self.__size -= 1

    def append(self, element):
        if self.__size >= len(self.__items):
            self.increase_capacity()

        self.__items[self.__size] = element
        self.__size += 1

    def increase_capacity(self):
        # увеличиваем длину массива в 2 раза
        self.__items = self.__items + [None] * len(self.__items)

    def ensure_capacity(self, number):
        if not isinstance(number, int):
            raise TypeError(f"Тип {number} должен быть int")

        if number < 0:
            raise ValueError(f"{number} должен быть больше нуля")

        if self.__capacity < number:
            self.__items = self.__items + [None] * (number - self.__size - 1)

            self.__capacity = number

    def trim_to_size(self):
        difference = len(self.__items) - self.__size
        trimmed_list = ArrayList(self.__size)

        if difference > 0:
            for i in range(self.__size):
                trimmed_list[i] = self.__items[i]

            self.__capacity = self.__size

            self.__items = trimmed_list

    def extend(self, components):
        if not isinstance(components, list):
            raise TypeError(f"Тип {components} должен быть list")

        items_length = len(components)

        for i in range(items_length):
            self.append(int(copy.copy(components[i])))

    def __iter__(self):
        for i in range(self.__size):
            yield self.__items[i]

    def __repr__(self):
        strings_array_list = map(lambda x: str(copy.copy(x)), self.__items)

        return "[" + ", ".join(strings_array_list) + "]"
