from collections.abc import Collection


class HashTable(Collection):
    def __init__(self, length=None):
        if length is None:
            self.__size = 10
        elif length <= 0:
            raise ValueError(f"Размер массива хэш-таблицы length: {length}, должен быть > 0")
        else:
            if not isinstance(length, int):
                raise TypeError(f"Тип размера массива хэш-таблицы length: {length}, должен быть int. "
                                f"Сейчас тип: {type(length).__name__}")

        self.__items = [None] * length

        # Атрибут, который хранит количество элементов в хэш-таблице
        self.__elements_quantity = 0

    @property
    def elements_quantity(self):
        return self.__elements_quantity

    # Получение размера хэш-таблицы:
    def __len__(self):
        return len(self.__items)

    # Метод для вычисления индекса:
    def __count_index(self, element):
        return abs(hash(element) % len(self.__items))

    def put_object(self, element):
        index = self.__count_index(element)

        if self.__items[index] is None:
            self.__items[index] = [element]

            self.__elements_quantity += 1
        else:
            self.__items[index].append(element)

            self.__elements_quantity += 1

    def __getitem__(self, index):
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

        return self.__items[index]

    def __contains__(self, element):
        index = self.__count_index(element)

        if self.__items[index] is not None:
            return element in self.__items[index]

        return False

    # Удаление элемента по значению. Если удалили, то выдает True, иначе - False
    def delete_element(self, element):
        index = self.__count_index(element)

        if self.__items[index] is None:
            return False
        elif len(self.__items[index]) == 1 and self.__items[index][0] == element:
            self.__items[index] = None

            self.__elements_quantity -= 1

            return True
        elif len(self.__items[index]) > 1:
            element_was_deleted = False

            if self.__items[index][len(self.__items[index]) - 1] == element and element_was_deleted is False:
                self.__items[index][len(self.__items[index]) - 1] = None

                self.__elements_quantity -= 1

                element_was_deleted = True
            else:
                for i in range(len(self.__items[index]) - 1):
                    if self.__items[index][i] == element and element_was_deleted is False:
                        self.__items[index][i] = None

                        self.__elements_quantity -= 1

                        element_was_deleted = True

                    # Перемещение элементов после индекса i на (i - 1)
                    if element_was_deleted is True:
                        self.__items[index][i] = self.__items[index][i + 1]

            # Урезание размера списка:
            if element_was_deleted is True:
                self.__items[index] = self.__items[index][0: len(self.__items[index]) - 1]
                return True

            return False
        else:
            return False

    def __iter__(self):
        for i in range(len(self.__items)):
            if self.__items[i] is None:
                continue

            for element in self.__items[i]:
                if element is None:
                    continue
                else:
                    yield element

    def __repr__(self):
        strings_list = map(str, self.__items)

        return "[" + ", ".join(strings_list) + "]"
