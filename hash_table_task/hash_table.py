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

        self.__lists = [None] * capacity

        # Атрибут, который хранит количество элементов в хэш-таблице
        self.__size = 0

    # Получение количества элементов в хэш-таблице:
    def __len__(self):
        return self.__size

    # Метод для вычисления индекса:
    def __get_index(self, element):
        return abs(hash(element) % len(self.__lists))

    def add_element(self, element):
        index = self.__get_index(element)

        if self.__lists[index] is None:
            self.__lists[index] = [element]
        else:
            self.__lists[index].append(element)

        self.__size += 1

    def __contains__(self, element):
        index = self.__get_index(element)

        # Проверка,что запрашиваемый список в хэш-таблице не None, иначе код упадёт
        if self.__lists[index] is None:
            return False

        for list_element in self.__lists[index]:
            if element == list_element:
                return True

    # Удаление элемента по значению. Если удалили, то выдает True, иначе - False
    def delete(self, element):
        index = self.__get_index(element)

        if self.__lists[index] is None:
            return False

        try:
            self.__lists[index].remove(element)
            self.__size -= 1

            return True
        except ValueError:
            return False

    def __iter__(self):
        for list_element in self.__lists:
            if list_element is not None:
                for element in list_element:
                    yield element

    def __repr__(self):
        strings_list = map(str, self.__lists)

        return "[" + ", ".join(strings_list) + "]"
