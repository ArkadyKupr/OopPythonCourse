from list_item import ListItem
from singly_linked_list import SinglyLinkedList

next_item = ListItem(50, None)

next_item = ListItem(50, next_item)

next_item = ListItem(20, next_item)

next_item = ListItem(10, next_item)

next_item = ListItem(1000, next_item)

user_list = SinglyLinkedList(next_item, 10)

print("Получение размера списка:", user_list.get_length())

print("Получение значения первого элемента:", user_list.get_first_item())

print("Получение значения по указанному индексу", user_list.get_item(3))

user_list.change_item(2, 2000)

print("Изменение значения по указанному индексу:", user_list.get_item(3))

# 5)  Удаление элемента по индексу, пусть выдает значение элемента:
print("Удаление элемента по индексу:")
user_list.print_items()
user_list.delete_item(2)
user_list.print_items()
print("Удалили значение элемента:", user_list.delete_item(2))

# 6)  Вставка элемента в начало списка:
user_list.insert_item_in_start(2)
user_list.print_items()
print("Получение значения первого элемента:", user_list.get_first_item())

# 7)  Вставка элемента по индексу:
user_list.insert_items(2, 67)
user_list.print_items()

print("Список:")
user_list.insert_item_in_start(6)
user_list.print_items()

# 8)  Удаление узла по значению, пусть выдает True, если элемент был удален:
user_list.delete_item_according_data(2)

# 9)  Удаление первого элемента, пусть выдает значение элемента:
print("Получение значения первого удаленного элемента:", user_list.delete_first_item())

# 10) Разворот списка за линейное время:
print("Разворот списка за линейное время:")
user_list.reverse()
# Печать списка:
user_list.print_items()

# 11) Копирование списка:
print("Копирование списка:")
copy = user_list.copy()
copy.print_items()
