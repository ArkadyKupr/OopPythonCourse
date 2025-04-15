from collections.abc import Collection, Hashable


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
    def _get_index(self, hash_list):
        # Вычисление hash-кода для элемента типа list
        if not isinstance(hash_list, Hashable):
            raise TypeError(f"Тип объекта: {hash_list}, не хешируемый")

        return abs(hash(hash_list) % len(self.__lists))

    def insert_element(self, element):
        index = self._get_index(element)

        if self.__lists[index] is None:
            self.__lists[index] = [element]
        else:
            self.__lists[index].append(element)

        self.__size += 1

    def __contains__(self, element):
        if element is None:
            return ValueError("Передаваемый элемент не должен быть None")

        index = self._get_index(element)

        for element in self.__lists[index]:
            return element in self.__lists[index]

    # Удаление элемента по значению. Если удалили, то выдает True, иначе - False
    def delete(self, element):
        index = self._get_index(element)

        if self.__lists[index] is None:
            return False

        if element in self.__lists[index]:
            self.__lists[index].remove(element)
            self.__size -= 1

            return True

        return False

    def __iter__(self):
        for hash_list in self.__lists:
            if hash_list is not None:
                if not isinstance(hash_list, Hashable):
                    yield hash_list
                else:
                    for element in hash_list:
                        if element is not None:
                            yield element
                        else:
                            yield None



            else:
                yield None

    def __repr__(self):
        strings_list = map(str, self.__lists)

        return "[" + ", ".join(strings_list) + "]"
