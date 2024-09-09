from collections.abc import MutableSequence


class ArrayList(MutableSequence):
    def __init__(self, size=None):
        if size is None:
            self.__size = 10
        else:
            if not isinstance(size, int):
                raise TypeError(f"Тип {size} должен быть int")

            if size < 0:
                raise ValueError(f"Вместимость должна быть >= 0. Передано значение: {size}")

            self.__size = size

        self.__items = [None] * self.__size
        self.__count = 0

    def __len__(self):
        return len(self.__items)

    # Проверка, что переданный индекс item-а в списке имеет тип int
    # Проверка, что переданный индекс item-а не выходит за диапазон допустимых значений списка
    def __check_item_index(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип {index} должен быть int. Сейчас тип: {type(index.__name__)}")

        if index < -len(self.__items) or index >= len(self.__items):
            raise ValueError(f"Индекс: {index}, должен лежать в диапазоне "
                             f"[-{len(self.__items)}, {len(self.__items) - 1}]")

    def __getitem__(self, slice_array):
        if isinstance(slice_array, slice):
            start = slice_array.start
            stop = slice_array.stop
            step = slice_array.step

            if step is None:
                step = 1

            if start is None:
                start = 0

            if stop is None:
                stop = len(self.__items) - 1

            # Поддержка отрицательных значений индексов:
            if start < 0 and stop < 0:
                start += len(self.__items)
                stop += len(self.__items)

            # Поддержка отрицательных step:
            if step < 0:
                copy = start
                start = stop
                stop = copy

            self.__check_item_index(start)
            self.__check_item_index(stop)

            slice_list = []

            for i in range(start, stop, step):
                slice_list.append(self.__items[i])

            return slice_list
        else:
            self.__check_item_index(slice_array)

            # Поддержка отрицательных индексов
            if slice_array < 0:
                slice_array += len(self.__items)

        return self.__items[slice_array]

    def __setitem__(self, index, value):
        self.__check_item_index(index)

        # Поддержка отрицательных индексов
        if index < 0:
            index += self.__size

        self.__items[index] = value

        self.__count += 1

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
        self.__size = len(self.__items)

        return deleted_item

    def append(self, element):
        if self.__count >= len(self.__items):
            self.__increase_capacity()

        self.__items[self.__count] = element
        self.__count += 1

    # Увеличение длины массива в 2 раза
    def __increase_capacity(self):
        # Увеличение длины пустого массива
        if len(self.__items) == 0:
            self.__items += [None] * 10

        # увеличиваем длину массива в 2 раза
        self.__items += [None] * len(self.__items)

        self.__size = len(self.__items)

    # Метод гарантирует, что вместимость списка будет >= указанного числа
    def ensure_capacity(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError(f"Тип {capacity} должен быть int")

        if len(self.__items) < capacity:
            self.__items += [None] * (capacity - len(self.__items))

        self.__size += (capacity - len(self.__items))

    # Метод урезает внутренний массив до размера списка. Полезно, если в списке было много элементов, а стало мало
    def trim_to_size(self):
        if self.__count == 0:
            self.__items = []

        self.__items = self.__items[0: self.__count]

    # Метод, который добавляет в список сразу большое количество элементов
    def extend(self, components):
        if not isinstance(components, (list, tuple, dict, set, ArrayList)):
            raise TypeError(f"Тип {components} должен быть коллекцией или принадлежать классу ArrayList. "
                            f"Сейчас тип: {type(components).__name__}")

        self.trim_to_size()

        for component in components:
            self.__items.append(component)
            self.__count += 1

        self.__size = len(self.__items)

    def copy(self):
        copied_list = ArrayList(0)

        for element in self.__items:
            copied_list.__items.append(element)
            copied_list.__count += 1

        copied_list.__size = len(copied_list)

        return copied_list

    def __delitem__(self, index):
        self.__check_item_index(index)

        # Поддержка отрицательных индексов
        if index < 0:
            index += len(self.__items)

        if self.__count == 1:
            self.__items = []

        for i in range(index, self.__count - 1):
            self.__items[i] = self.__items[i + 1]

        self.__items[self.__count - 1] = None

        self.__count -= 1

    def insert(self, index, data):
        self.__check_item_index(index)

        if not isinstance(index, int):
            raise TypeError(f"Тип {index} не является int")

        if index < -self.__count or index > self.__count:
            raise IndexError(f"Указанный индекс должен быть в диапазоне [{-self.__count}, {self.__count}]"
                             f"Сейчас передано значение: {index}")

        # Поддержка отрицательных индексов
        if index < 0:
            index += self.__size

        self.__items.append(None)

        self.__count += 1

        for i in range(self.__count, index, -1):
            self.__items[i] = self.__items[i - 1]

        self.__items[index] = data

        self.trim_to_size()

    def __iter__(self):
        for i in range(len(self)):
            yield self.__items[i]

    def __repr__(self):
        string = map(lambda x: str(x), self.__items[0: self.__count])

        return "[" + ", ".join(string) + "]"

    def __eq__(self, other):
        if not isinstance(self, ArrayList):
            raise TypeError(f"Объект {self} не являетя объектом класса ArrayList")

        if not isinstance(other, ArrayList):
            raise TypeError(f"Объект {other} не являетя объектом класса ArrayList")

        return self.__items == other.__items

    def __hash__(self):
        return hash(tuple(self.__items))

    def __iadd__(self, other):
        if not isinstance(other, ArrayList):
            raise TypeError(f"Объект {other} не являетя объектом класса ArrayList")

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
