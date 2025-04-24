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
    def __get_index(self, hash_list):
        # Вычисление hash-кода для элемента типа list
        """if not isinstance(hash_list, Hashable):
            raise TypeError(f"Тип объекта: {hash_list}, не хешируемый")"""

        return abs(hash(hash_list) % len(self.__lists))

    def insert_element(self, element):
        index = self.__get_index(element)

        if self.__lists[index] is None:
            self.__lists[index] = [element]
        else:
            self.__lists[index].append(element)

        self.__size += 1

    def __contains__(self, user_element):
        # Проверка,что пустой список содержится в хэш-таблице:
        if isinstance(user_element, list) and len(user_element) == 0:
            for element in self.__lists:
                if isinstance(element, list) and len(element) == 0:
                    return True

            return False

        # Проверка,что None содержится в хэш-таблице:
        if user_element is None:
            for element in self.__lists:
                if element is None:
                    return True

        index = self.__get_index(user_element)

        for user_element in self.__lists[index]:
            return user_element in self.__lists[index]

    # Удаление элемента по значению. Если удалили, то выдает True, иначе - False
    def delete(self, user_element):
        # Удаление пустого списка в хэш-таблице:
        if isinstance(user_element, list) and len(user_element) == 0:
            element_deleted = False

            for i, element in enumerate(self.__lists):
                if isinstance(element, list) and len(element) == 0:
                    self.__lists[i] = None
                    element_deleted = True

                if i == self.__size - 1 and element_deleted:
                    return True

            return False

        index = self.__get_index(user_element)

        if self.__lists[index] is None:
            return False

        if user_element in self.__lists[index]:
            self.__lists[index].remove(user_element)
            self.__size -= 1
            return True

        return False

    def __iter__(self):
        for hash_list in self.__lists:
            if hash_list is not None:
                if isinstance(hash_list, list) and len(hash_list) == 0:
                    yield None

                for element in hash_list:
                    yield element
            else:
                yield None

    def __repr__(self):
        strings_list = map(str, self.__lists)

        return "[" + ", ".join(strings_list) + "]"
