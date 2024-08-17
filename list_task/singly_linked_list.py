from list_task.list_item import ListItem


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    # 1) Получение размера списка:
    def __len__(self):
        return self.__count

    # 2) Получение значения первого элемента:
    def get_first(self):
        if self.__head is None:
            raise IndexError("Список пустой и не имеет первого элемента")

        return self.__head.data

    # Проверка корректности указанного индекса
    def __check_item_index(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип {index} должен быть int. Сейчас тип: {type(index).__name__}")

        if index < -self.__count or index >= self.__count:
            raise IndexError(f"Указанный индекс должен быть в диапазоне [{-self.__count}, {self.__count - 1}]"
                             f"Сейчас передано значение: {index}")

    @staticmethod
    def __iterate_to_item(index, item):
        i = 0

        while i < index:
            item = item.next
            i += 1

    # 3) Получение значения по указанному индексу:
    def __getitem__(self, index):
        self.__check_item_index(index)

        # Поддержка отрицательных индексов
        if index < 0:
            index += self.__count

        item = self.__head

        self.__iterate_to_item(index, item)

        return item.data

    # 4) Изменение значения по указанному индексу:
    def __setitem__(self, index, data):
        self.__check_item_index(index)

        # Поддержка отрицательных индексов
        if index < 0:
            index += self.__count

        item = self.__head

        self.__iterate_to_item(index, item)

        return item.data

    # 5) Удаление элемента по индексу, пусть выдает значение элемента:
    def __delitem__(self, index):
        self.__check_item_index(index)

        # Поддержка отрицательных индексов
        if index < 0:
            index += self.__count

        item = self.__head
        i = 0
        deleted_data = 0

        if index == 0:
            deleted_data = item.data
            self.__head = item.next
            self.__count -= 1
        else:
            while i < self.__count:
                if i == index - 1:
                    deleted_data = item.next.data
                    item.next = item.next.next

                    i += 1
                    self.__count -= 1
                    break

                item = item.next
                i += 1

        return deleted_data

    # 6) Вставка элемента в начало списка:
    def add_first(self, data):
        self.__head = ListItem(data, self.__head)

        self.__count += 1

    # 7) Вставка элемента по индексу:
    def insert(self, index, data):
        if not isinstance(index, int):
            raise TypeError(f"Тип {index} не является int")

        if index < -self.__count or index > self.__count:
            raise IndexError(f"Указанный индекс должен быть в диапазоне [{-self.__count}, {self.__count}]"
                             f"Сейчас передано значение: {index}")

        # Поддержка отрицательных индексов
        if index < 0:
            index += self.__count

        item = self.__head
        i = 0

        if index == 0:
            self.__head = ListItem(data, item)

            self.__count += 1
        else:
            while i <= index:
                if i == index - 1:
                    item.next = ListItem(data, item.next)

                    self.__count += 1
                    break

                item = item.next
                i += 1

    # 8) Удаление узла по значению, пусть выдает True, если элемент был удален:
    def delete_by_data(self, data):
        if self.__count == 0:
            raise IndexError("Список пустой и не имеет первого элемента")

        if self.__head.data == data:
            self.__head = self.__head.next
            self.__count -= 1

            return True

        previous_item = self.__head
        current_item = self.__head.next

        while current_item is not None:
            if current_item.data == data:
                previous_item.next = current_item.next

                self.__count -= 1
                return True

            previous_item = previous_item.next
            current_item = current_item.next

        return False

    # 9) Удаление первого элемента, пусть выдает значение элемента:
    def delete_first(self):
        if self.__head is None:
            raise IndexError("Список пустой и не имеет первого элемента")

        item = self.__head
        deleted_data = item.data
        self.__head = item.next

        self.__count -= 1

        return deleted_data

    # 10) Разворот списка за линейное время:
    def reverse(self):
        item = self.__head
        previous_item = None

        while item is not None:
            next_item = item.next
            item.next = previous_item
            previous_item = item
            item = next_item

        self.__head = previous_item

    # 11) Копирование списка:
    def copy(self):
        if self.__head is None:
            raise IndexError("Список пустой и не имеет первого элемента")

        item = self.__head

        copied_list = SinglyLinkedList()
        copied_list.__count = self.__count

        copied_item = ListItem(item.data)
        copied_list.__head = copied_item

        item = item.next

        while item is not None:
            copied_item.next = ListItem(item.data)
            copied_item = copied_item.next

            item = item.next

        return copied_list

    # Печать списка для тестирования программы
    def __repr__(self):
        item = self.__head

        numbers_string = "["

        for i in range(self.__count):
            numbers_string += str(item.data)

            if i != self.__count - 1:
                numbers_string += ", "

            item = item.next

        numbers_string += "]"

        return numbers_string
