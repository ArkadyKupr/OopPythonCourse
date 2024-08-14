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
    def __check_index_1(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип {index} должен быть int")

        if index < 0 or index >= self.__count:
            raise IndexError(f"Указанный индекс должен быть в диапазоне [0, {self.__count - 1}]")

    def __check_index_2(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип {index} не является int")

        if index < 0 or index > self.__count:
            raise IndexError(f"Указанный индекс должен быть в диапазоне [0, {self.__count}]")

    # Проверка корректности переданного значения
    def __check_data(self, data):
        if not isinstance(data, (int, float)):
            raise TypeError(f"Тип {data} должен быть int или float")

    # 3) Получение значения по указанному индексу:
    def __getitem__(self, index):
        self.__check_index_1(index)

        item = self.__head
        i = 0

        while i <= index:
            if i == index:
                return item.data

            item = item.next
            i += 1

    # 4) Изменение значения по указанному индексу:
    def __setitem__(self, index, data):
        self.__check_index_1(index)
        self.__check_data(data)

        item = self.__head
        i = 0

        while i <= index:
            if i == index:
                item.data = data

            item = item.next
            i += 1

    # 5)  Удаление элемента по индексу, пусть выдает значение элемента:
    def __delitem__(self, index):
        self.__check_index_1(index)

        item = self.__head
        i = 0
        deleted_data = 0
        items_quantity = self.__count

        while i < items_quantity:
            if index == 0:
                deleted_data = item.data
                self.__head = item.next
                self.__count -= 1
                break

            if i == index - 1:
                deleted_data = item.next.data
                item.next = item.next.next

                i += 1
                self.__count -= 1

            item = item.next
            i += 1

        return deleted_data

    # 6)  Вставка элемента в начало списка:
    def insert_in_start(self, data):
        self.__check_data(data)

        new_item = ListItem(data, self.__head)
        self.__head = new_item

        self.__count += 1

    # 7)  Вставка элемента по индексу:
    def insert(self, index, data):
        self.__check_index_2(index)
        self.__check_data(data)

        item = self.__head
        i = 0

        while i <= index:
            if index == 0:
                self.__head = ListItem(data, item)

                self.__count += 1
                break

            if i == index - 1:
                reference = item.next
                item.next = ListItem(data)
                item.next.next = reference

                self.__count += 1
                break

            item = item.next
            i += 1

    # 8)  Удаление узла по значению, пусть выдает True, если элемент был удален:
    def delete_by_data(self, data):
        self.__check_data(data)

        items_quantity = self.__count
        item = self.__head
        i = 0

        while i < items_quantity:
            if i == 0 and item.data == data:
                reference = item.next
                self.__head = reference

                self.__count -= 1

                return True

            if item.next.data == data:
                if i == 0:
                    reference = item.next
                    self.__head = reference

                    self.__count -= 1

                    return True

                item.next = item.next.next

                self.__count -= 1

                return True

            if item.next.next is None:
                return False

            item = item.next
            i += 1

    # 9)  Удаление первого элемента, пусть выдает значение элемента:
    def delete_first(self):
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
        item = self.__head
        copied_list = SinglyLinkedList()

        copied_item = ListItem(item.data)

        copied_list.__head = copied_item
        copied_list.__count = self.__count

        while item.next is not None:
            copied_item.next = ListItem(item.next.data)
            item = item.next
            copied_item = copied_item.next

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

        return f"{numbers_string}"
