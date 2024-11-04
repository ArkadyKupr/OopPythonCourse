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
        self.__check_list_emptiness()

        return self.__head.data

    # Проверка корректности указанного индекса
    def __check_item_index(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Тип индекса index: {index}, должен быть int. Сейчас тип: {type(index).__name__}")

        if index < -self.__count or index >= self.__count:
            raise IndexError(f"Указанный индекс index, должен быть в диапазоне [{-self.__count}, {self.__count - 1}]"
                             f"Сейчас передано значение: {index}")

    # Проход по списку до элемента с индексом - index и получение этого элемента
    def __get_item(self, index):
        item = self.__head
        i = 0

        # Поддержка отрицательных значений индекса:
        if index < 0:
            index += self.__count

        while i < index:
            item = item.next
            i += 1

        return item

    # Проверка, что список не пустой
    def __check_list_emptiness(self):
        if self.__head is None:
            raise IndexError("Список пустой и не имеет первого элемента")

    # 3) Получение значения по указанному индексу:
    def __getitem__(self, index):
        self.__check_item_index(index)

        return self.__get_item(index).data

    # 4) Изменение значения по указанному индексу:
    def __setitem__(self, index, data):
        self.__check_item_index(index)

        self.__get_item(index).data = data

    # 5) Удаление элемента по индексу, пусть выдает значение элемента:
    def __delitem__(self, index):
        self.__check_item_index(index)

        if index == 0:
            return self.delete_first()

        previous_item = self.__get_item(index - 1)
        deleted_data = previous_item.next.data
        previous_item.next = previous_item.next.next

        self.__count -= 1

        return deleted_data

    # 6) Вставка элемента в начало списка:
    def add_first(self, data):
        self.__head = ListItem(data, self.__head)

        self.__count += 1

    # 7) Вставка элемента по индексу:
    def insert(self, index, data):
        if not isinstance(index, int):
            raise TypeError(f"Тип индекса index: {index}, не является int")

        if index < -self.__count or index > self.__count:
            raise IndexError(f"Указанный индекс index должен быть в диапазоне [{-self.__count}, {self.__count}]"
                             f"Сейчас передано значение: {index}")

        if index == 0:
            self.add_first(data)
        else:
            previous_item = self.__get_item(index - 1)
            previous_item.next = ListItem(data, previous_item.next)

            self.__count += 1

    # 8) Удаление узла по значению, пусть выдает True, если элемент был удален:
    def delete_by_data(self, data):
        if self.__head is None:
            return False

        if self.__head.data == data:
            self.delete_first()

            return True

        previous_item = self.__head
        current_item = self.__head.next

        while current_item is not None:
            if current_item.data == data:
                previous_item.next = current_item.next

                self.__count -= 1
                return True

            previous_item = current_item
            current_item = current_item.next

        return False

    # 9) Удаление первого элемента, пусть выдает значение элемента:
    def delete_first(self):
        self.__check_list_emptiness()

        deleted_data = self.__head.data
        self.__head = self.__head.next

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
        copied_list = SinglyLinkedList()
        copied_list.__count = self.__count

        if self.__head is None:
            return copied_list

        copied_item = ListItem(self.__head.data)
        copied_list.__head = copied_item

        item = self.__head.next

        while item is not None:
            copied_item.next = ListItem(item.data)
            copied_item = copied_item.next

            item = item.next

        return copied_list

    # Печать списка для тестирования программы
    def __repr__(self):
        item = self.__head

        items_list = []

        while item is not None:
            items_list.append(str(item.data))

            item = item.next

        return "[" + ", ".join(items_list) + "]"
