from collections.abc import MutableSequence
from multipledispatch import dispatch


class ArrayList(MutableSequence):
    @dispatch(int)
    def __init__(self, size=None):
        if size is None:
            size = 10
        else:
            if not isinstance(size, int):
                raise TypeError(f"Тип size: {size}, должен быть int")

            if size < 0:
                raise ValueError(f"Вместимость size должна быть >= 0. Передано значение size: {size}")

        self.__items = [None] * size
        self.__count = 0

    # Для варианта со slice в __getitem__, где нужно выдавать экземпляр своего списка вместо стандартного
    # В списке должны допускаться любые типы элементов
    @dispatch(list)
    def __init__(self, items):
        if not isinstance(items, list):
            raise TypeError(f"Объект items: {items}, не является списком. "
                            f"Сейчас тип items: {type(items).__name__}")

        self.__count = len(items)
        self.__items = items.copy()

    def __len__(self):
        return self.__count

    # Проверка, что переданный индекс item-а в списке имеет тип int
    # Проверка, что переданный индекс item-а не выходит за диапазон допустимых значений списка
    def __check_item_index(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип index: {index}, должен быть int. Сейчас тип: {type(index.__name__)}")

        if index < -self.__count or index >= self.__count:
            raise ValueError(f"Индекс index: {index}, должен лежать в диапазоне "
                             f"[-{self.__count}, {self.__count - 1}]")

    def __getitem__(self, key):
        if isinstance(key, slice):
            slice_list = self.__items[key.start:key.stop:key.step]

            return ArrayList(slice_list)

        self.__check_item_index(key)

        # Поддержка отрицательных индексов
        if key < 0:
            key += len(self.__items)

        return self.__items[key]

    def __setitem__(self, index, item):
        self.__check_item_index(index)

        # Поддержка отрицательных индексов
        if index < 0:
            index += len(self.__items)

        self.__items[index] = item

    def append(self, item):
        # В списке должны допускаться любые типы элементов
        if self.__count >= len(self.__items):
            self.__increase_capacity()

        self.__items[self.__count] = item

        self.__count += 1

    # Увеличение длины массива в 2 раза
    def __increase_capacity(self):
        # Увеличение длины пустого массива
        if len(self.__items) == 0:
            self.__items = [None] * 10
        else:
            self.__items += [None] * len(self.__items)

    # Метод гарантирует, что вместимость списка будет >= указанного числа
    def ensure_capacity(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError(f"Тип capacity: {capacity}, должен быть int")

        if len(self.__items) < capacity:
            self.__items += [None] * (capacity - len(self.__items))

    # Метод урезает внутренний массив до размера списка. Полезно, если в списке было много элементов, а стало мало
    def trim_to_size(self):
        if self.__count < len(self.__items):
            self.__items = self.__items[0: self.__count]

    # Функция, которая возвращает True, если по типу можно проитерироваться, иначе - False
    @staticmethod
    def __is_iterable(components):
        try:
            iter(components)
            return True
        except TypeError:
            return False

    def copy(self):
        copied_list = []

        for item in self.__items:
            copied_list.append(item)

        return ArrayList(copied_list)

    def __delitem__(self, index):
        self.__check_item_index(index)

        # Поддержка отрицательных индексов
        if index < 0:
            index += len(self.__items)

        for i in range(index, self.__count - 1):
            self.__items[i] = self.__items[i + 1]

        self.__items[self.__count - 1] = None

        self.__count -= 1

    def insert(self, index, item):
        if not isinstance(index, int):
            raise TypeError(f"Тип index: {index}, не является int")

        # insert допускает вставку в конец списка, поэтому index варьируется до self.__count включительно
        if index < -self.__count or index > self.__count:
            raise IndexError(f"Указанный индекс index должен быть в диапазоне [{-self.__count}, {self.__count}] "
                             f"Сейчас передано значение index: {index}")

        # Поддержка отрицательных индексов
        if index < 0:
            index += len(self.__items)

        if index == len(self.__items):
            self.__increase_capacity()

        for i in range(self.__count, index, -1):
            self.__items[i] = self.__items[i - 1]

        self.__items[index] = item

        self.__count += 1

    def __iter__(self):
        for i in range(len(self.__items)):
            yield self.__items[i]

    def __repr__(self):
        items_list = map(lambda x: str(x), self.__items[0: len(self.__items)])

        return "[" + ", ".join(items_list) + "]"

    def __eq__(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError(f"Объект other: {other}, не является объектом класса ArrayList")

        for i in range(self.__count):
            if self.__items[i] != other.__items[i]:
                return False

        return True

    def __hash__(self):
        return hash(tuple(self.__items))

    def reverse(self):
        array_list_middle_index = self.__count // 2

        for i in range(array_list_middle_index):
            copy = self.__items[i]
            self.__items[i] = self.__items[self.__count - 1 - i]
            self.__items[self.__count - 1 - i] = copy
