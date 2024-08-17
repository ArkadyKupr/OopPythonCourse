class HashTable:
    def __init__(self, size=None):
        if size is None:
            self.__size = 100
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
            self.__items[index] = []
            self.__items[index].append([key, value])
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
            for item in self.__items[index]:
                if item[0] == key and item[1] == value:
                    return True

            return False

        raise KeyError(f"Хэш-таблица не содержит пару: ({key}, {value})")

    def __hash__(self):
        return hash(tuple(self))

    def __len__(self):
        return self.__size

    @property
    def size(self):
        return self.__size

    def __iter__(self):
        for i in range(self.size):
            yield self.__items[i]
