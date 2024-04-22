import copy
from list_item import ListItem


class SinglyLinkedList:
    def __init__(self, head, count):
        self.__head = head
        self.__count = count

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head):
        self.__head = head

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def get_count(self):
        return self.__count

    # 1) Получение размера списка:
    def get_length(self):
        last_reference = self.__head
        current_length = 0

        while last_reference is not None:
            current_length += 1
            last_reference = last_reference.next

        return current_length

    # 2) Получение значения первого элемента:
    def get_first_item(self):
        if self.__head is None:
            raise ReferenceError(f"Список не имеет первого элемента")

        return self.__head.data

    # 3) Получение значения по указанному индексу:
    def get_item(self, index):
        last = self.__head
        current_index = 0
        while current_index <= index:
            if current_index == index:
                return last.data

            current_index += 1
            last = last.next

    # 4) Изменение значения по указанному индексу:
    def change_item(self, index, new_data):
        last = self.__head
        current_index = 0

        while current_index <= index:
            if current_index == index:
                last.data = new_data

            current_index += 1
            last = last.next

    # 5)  Удаление элемента по индексу, пусть выдает значение элемента:
    def delete_item(self, index):
        current_item = self.__head
        current_index = 0
        next_item = None
        deleted_data = 0

        while current_index <= index + 1:
            if current_index == index:
                deleted_data = current_item.data

            if current_index == index + 1:
                next_item = current_item
                break

            current_item = current_item.next

            current_index += 1

        current_item = self.__head
        current_index = 0

        while current_index <= index:

            if current_index == index - 1:
                current_item.next = next_item

            current_item = current_item.next

            current_index += 1

        return deleted_data

    # 6)  Вставка элемента в начало списка:
    def insert_item_in_start(self, data):
        head = self.__head

        new_item = ListItem(data, head)

        self.head = new_item

    # 7)  Вставка элемента по индексу:
    def insert_items(self, index, data):
        current_item = self.__head
        item = ListItem(data, None)
        current_index = 0

        while current_index <= index:

            if current_index == index:
                item.next = current_item
                break

            current_item = current_item.next

            current_index += 1

        current_item = self.__head
        current_index = 0

        while current_index <= index:

            if current_index == index - 1:
                current_item.next = item

            current_item = current_item.next

            current_index += 1

    # 8)  Удаление узла по значению, пусть выдает True, если элемент был удален:
    def delete_item_according_data(self, data):
        current_item = self.__head
        index = 0
        deleted_item_index = 0
        next_item = None

        while current_item is not None:
            if current_item.data == data:
                next_item = current_item.next
                deleted_item_index = index
                break

            current_item = current_item.next

            index += 1

        current_item = self.__head
        index = 0
        previous_item_index = deleted_item_index - 1

        while index <= previous_item_index:
            if index == previous_item_index:
                current_item.next = next_item

                return True

            current_item = current_item.next

            index += 1

        return False

    # 9)  Удаление первого элемента, пусть выдает значение элемента:
    def delete_first_item(self):
        head = self.__head

        next_item = head.next
        deleted_data = head.data
        self.__head = next_item

        return deleted_data

    # 10) Разворот списка за линейное время:
    def reverse(self):
        current_item = self.__head
        previous_item = None

        while current_item is not None:
            next_item = current_item.next
            current_item.next = previous_item
            previous_item = current_item
            current_item = next_item

        self.__head = previous_item

    # 11) Копирование списка:
    def copy(self):
        self.reverse()

        current_item = self.__head
        copied_previous_item = None

        while current_item is not None:
            copied_next_item = ListItem(copy.deepcopy(current_item.data), copied_previous_item)
            copied_previous_item = copied_next_item
            current_item = current_item.next

        new_current_item = SinglyLinkedList(copied_previous_item, copy.deepcopy(self.__count))

        self.reverse()

        return new_current_item

    # Печать списка для тестирования программы
    def print_items(self):
        current_item = self.__head

        while current_item is not None:
            print(current_item.data, end=' ')

            current_item = current_item.next

        print()

    # 11) Копирование списка:
    def copy_with_two_references(self):
        self.reverse()

        current_item = self.__head
        copied_previous_item = None

        while current_item is not None:
            copied_next_item = ListItem(copy.deepcopy(current_item.data), copied_previous_item)
            copied_previous_item = copied_next_item
            current_item = current_item.next

        new_current_item = SinglyLinkedList(copied_previous_item, copy.deepcopy(self.__count))

        self.reverse()

        return new_current_item
