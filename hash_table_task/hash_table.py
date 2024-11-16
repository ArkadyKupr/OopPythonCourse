from collections.abc import Collection


class HashTable(Collection):
    def __init__(self, capacity=None):
        if capacity is None:
            capacity = 10

        if not isinstance(capacity, int):
            raise TypeError(f"Тип размера массива хэш-таблицы capacity: {capacity}, должен быть int. "
                            f"Сейчас тип: {type(capacity).__name__}")
        if capacity <= 0:
            raise ValueError(f"Размер массива хэш-таблицы capacity: {capacity}, должен быть > 0")

        self.__items = [None] * capacity

        # Атрибут, который хранит количество элементов в хэш-таблице
        self.__size = 0

    # Получение количества элементов в хэш-таблице:
    def __len__(self):
        return self.__size

    # Метод для вычисления индекса:
    def __get_index(self, item):
        # Вычисление hash-кода для элемента типа list
        if isinstance(item, list):
            return abs(self.hash_for_list(item) % len(self.__items))

        # Вычисление hash-кода для элемента типа set
        if isinstance(item, set):
            return abs(self.hash_for_set(item) % len(self.__items))

        # Вычисление hash-кода для элемента типа dict
        if isinstance(item, dict):
            return abs(self.hash_for_set(item) % len(self.__items))

        return abs(hash(item) % len(self.__items))

    def insert_element(self, element):
        index = self.__get_index(element)

        if self.__items[index] is None:
            self.__items[index] = [element]
        else:
            self.__items[index].append(element)

        self.__size += 1

    """def __getitem__(self, index):
        if not self.__items[index]:
            return None

        if not isinstance(index, int):
            raise TypeError(f"Тип {index} должен быть int. Сейчас тип: {type(index).__name__}")

        if index < -len(self.__items) or index >= len(self.__items):
            raise IndexError(f"Указанный индекс index, должен быть в диапазоне "
                             f"[{-len(self.__items)}, {len(self.__items) - 1}]. "
                             f"Сейчас передано значение: {index}")

        # Поддержка отрицательных значений индекса:
        if index < 0:
            index += len(self.__items)

        return self.__items[index]"""

    def __contains__(self, element):
        index = self.__get_index(element)

        return element in self.__items[index]

    # Удаление элемента по значению. Если удалили, то выдает True, иначе - False
    def delete(self, element):
        index = self.__get_index(element)

        if self.__items[index] is None:
            return False

        for item in self.__items[index]:
            if item == element:
                self.__items[index].remove(item)

                # Замена item на None, если item - это пустой список
                if len(item) == 0:
                    self.__items[index] = None

                return True

    def __iter__(self):
        for element in self.__items:
            if element is None:
                yield None
            else:
                for subelement in element:
                    if subelement is not None:
                        yield subelement

    def __repr__(self):
        strings_list = map(str, self.__items)

        return "[" + ", ".join(strings_list) + "]"

    @staticmethod
    def hash_for_list(element):
        hash_sum = 0

        for item in element:
            hash_sum += hash(item)

        return hash_sum

    @staticmethod
    def hash_for_set(element):
        hash_sum = 0

        for item in element:
            hash_sum += hash(item)

        return hash_sum

    @staticmethod
    def hash_for_dict(element):
        hash_sum = 0

        for item in element:
            hash_sum += hash(item[0])
            hash_sum += hash(item[1])

        return hash_sum
