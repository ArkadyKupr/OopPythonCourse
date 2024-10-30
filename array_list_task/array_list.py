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
    @dispatch(list)
    def __init__(self, items):
        if not isinstance(items, list):
            raise TypeError(f"Объект items: {items}, не является списком. "
                            f"Сейчас тип items: {type(items).__name__}")

        if len(items) <= 0:
            raise ValueError("Размерность списка должна быть > 0, но передан список "
                             f"items с размерностью {len(items)}")

        for item in items:
            if not isinstance(item, (int, float)):
                raise TypeError(f"Тип всех элементов списка items: {items}, должен быть int или float. "
                                f"Сейчас тип item: {type(item).__name__}")

        self.__count = len(items)
        self.__items = items.copy()

    def __len__(self):
        return self.__count

    # Проверка, что переданный индекс item-а в списке имеет тип int
    # Проверка, что переданный индекс item-а не выходит за диапазон допустимых значений списка
    def __check_item_index(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип index: {index}, должен быть int. Сейчас тип: {type(index.__name__)}")

        if index < - len(self.__items) or index >= len(self.__items):
            raise ValueError(f"Индекс index: {index}, должен лежать в диапазоне "
                             f"[-{len(self.__items)}, {len(self.__items) - 1}]")

    def __getitem__(self, key):
        if isinstance(key, slice):
            user_list = []

            for i in range(len(self.__items)):
                user_list.append(self.__items[i])

            slice_list = user_list[key.start:key.stop:key.step]

            if len(slice_list) == 0:
                return None

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

        if index >= self.__count:
            raise IndexError(f"Указанный индекс index должен быть в диапазоне [{-self.__count}, {self.__count - 1}] "
                             f"Сейчас передано значение index: {index}")

        self.__items[index] = item

    # Функция удаление значения по индексу должна возвращать удаленное значение
    def pop(self, index):
        self.__check_item_index(index)

        # Поддержка отрицательных индексов
        if index < 0:
            index += len(self.__items)

        deleted_item = self[index]

        if index < self.__count - 1:
            for i in range(index, self.__count):
                self.__items[i] = self.__items[i + 1]

        self.__items[self.__count - 1] = None
        self.__count -= 1

        return deleted_item

    def append(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError(f"Тип item: {item}, должен быть int или float. Сейчас тип: {type(item.__name__)}")

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
            # увеличиваем длину массива в 2 раза
            self.__items += [None] * len(self.__items)

    # Метод гарантирует, что вместимость списка будет >= указанного числа
    def ensure_capacity(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError(f"Тип capacity: {capacity}, должен быть int")

        if len(self.__items) < capacity:
            self.__items += [None] * (capacity - len(self.__items))

    # Метод урезает внутренний массив до размера списка. Полезно, если в списке было много элементов, а стало мало
    def trim_to_size(self):
        self.__items = self.__items[0: self.__count]

    # Метод, который добавляет в список сразу большое количество элементов
    def extend(self, components):
        if not isinstance(components, (list, tuple, dict, set, ArrayList)):
            raise TypeError(f"Тип components: {components}, должен быть коллекцией или принадлежать классу ArrayList. "
                            f"Сейчас тип components: {type(components).__name__}")

        self.trim_to_size()

        for component in components:
            self.__items.append(component)
            self.__count += 1

    def copy(self):
        copied_list = ArrayList(len(self.__items))

        for item in self.__items:
            copied_list.__items.append(item)
            copied_list.__count += 1

        return copied_list

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

        if not isinstance(item, (int, float)):
            raise TypeError(f"Тип item: {item}, должен быть int или float. Сейчас тип: {type(item.__name__)}")

        # Поддержка отрицательных индексов
        if index < 0:
            index += len(self.__items)

        self.__items.append(None)

        for i in range(self.__count, index, -1):
            self.__items[i] = self.__items[i - 1]

        self.__items[index] = item

        self.__count += 1

        self.trim_to_size()

    def __iter__(self):
        for i in range(len(self)):
            yield self.__items[i]

    def __repr__(self):
        array_list = map(lambda x: str(x), self.__items[0: self.__count])

        return "[" + ", ".join(array_list) + "]"

    def __eq__(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError(f"Объект other: {other}, не являетя объектом класса ArrayList")

        return self.__items[0:self.__count] == other.__items[0:other.__count]

    def __hash__(self):
        return hash(tuple(self.__items[0:self.__count]))

    def __iadd__(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError(f"Объект other: {other}, не являетя объектом класса ArrayList")

        if self.__count < other.__count:
            difference = other.__count - self.__count

            for i in range(difference + 1):
                self.__items.append(0)

            for i in range(other.__count):
                self.__items[i] += other.__items[i]
        else:
            if self.__count >= other.__count:
                for i in range(other.__count):
                    self.__items[i] += other.__items[i]

        return self

    def reverse(self):
        array_list_middle = int(self.__count / 2)

        for i in range(array_list_middle):
            copy = self.__items[i]
            self.__items[i] = self.__items[self.__count - 1 - i]
            self.__items[self.__count - 1 - i] = copy
