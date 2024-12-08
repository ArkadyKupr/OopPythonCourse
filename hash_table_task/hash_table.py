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

        self.__items = [None] * capacity

        # Атрибут, который хранит количество элементов в хэш-таблице
        self.__size = 0

    # Получение количества элементов в хэш-таблице:
    def __len__(self):
        return self.__size

    # Метод для вычисления индекса:
    def __get_index(self, item):
        # Вычисление hash-кода для элемента типа list
        if not isinstance(item, Hashable):
            raise TypeError(f"Тип объекта: {item}, не хешируемый")

        return abs(hash(item) % len(self.__items))

    def insert_element(self, element):
        index = self.__get_index(element)

        if self.__items[index] is None:
            self.__items[index] = [element]
        else:
            self.__items[index].append(element)

        self.__size += 1

    def __contains__(self, element):
        if element is None:
            return ValueError("Передаваемый элемент не должен быть None")

        index = self.__get_index(element)

        return element in self.__items[index]

    # Удаление элемента по значению. Если удалили, то выдает True, иначе - False
    def delete(self, element):
        index = self.__get_index(element)

        if self.__items[index] is None:
            return False

        if element in self.__items[index]:
            self.__items[index].remove(element)
            self.__size -= 1

            return True

        return False

    def __iter__(self):
        for item in self.__items:
            if item is None:
                continue
            else:
                for element in item:
                    if element is not None:
                        yield element
                    else:
                        yield None

    def __repr__(self):
        strings_list = map(str, self.__items)

        return "[" + ", ".join(strings_list) + "]"
