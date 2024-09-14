from collections.abc import Collection


class HashTable(Collection):
    def __init__(self, size=None):
        if size is None:
            self.__size = 10
        else:
            if not isinstance(size, int):
                raise TypeError(f"Тип {size} должен быть int. Сейчас тип: {type(size).__name__}")

        if size < 0:
            raise ValueError(f"{size} должен быть > 0")

        self.__size = size

        self.__items = [None] * size

    def __setitem__(self, key, value):
        index = abs(hash(key) % len(self.__items))

        if self.__items[index] is None:
            self.__items[index] = [[key, value]]
        else:
            self.__items[index].append([key, value])

    def __getitem__(self, key):
        index = abs(hash(key) % len(self.__items))

        if self.__items[index]:
            return self.__items[index]

        raise KeyError(f"Хэш-таблица не содержит ничего по ключу: {key}")

    def __contains__(self, key, value):
        index = abs(hash(key) % len(self.__items))

        if self.__items[index] is not None:
            return [key, value] in self.__items[index]

        return False

    def __hash__(self):
        return hash(tuple(self))

    def __len__(self):
        return len(self.__items)

    @property
    def size(self):
        return self.__size

    def __iter__(self):
        for i in range(self.size):
            for j in range(len(self.__items[i])):
                yield self.__items[i][j]

    def __repr__(self):
        strings_list = map(str, self.__items)

        return "[" + ", ".join(strings_list) + "]"
