from list_task.singly_linked_list import SinglyLinkedList

# Создаем и заполняем односвязный список
user_list = SinglyLinkedList()

user_list.add_first(2)
user_list.add_first(3)
user_list.add_first(4)
user_list.add_first(9)

print("# 1) Получение размера списка:")
print("Размер списка:", len(user_list))
print()

print("# 2) Получение значения первого элемента:")
print("Значение первого элемента:", user_list.get_first())
print()

print("# 3) Получение значения по указанному индексу:")
print("Значение по указанному индексу:", user_list[-3])
print()

print("# 4) Изменение значения по указанному индексу:")
user_list[2] = 2000
print("Изменили значение на:", user_list[2])
print()

print("# 5)  Удаление элемента по индексу, пусть выдает значение элемента:")
print(user_list)
del user_list[1]
print("Удалили значение элемента:", user_list)
print(user_list)
print()

del user_list[-1]
print("Удалили значение элемента:", user_list)
print(user_list)
print()

print("# 6)  Вставка элемента в начало списка:")
user_list.add_first(2)
print(user_list)
print("Получение значения первого элемента:", user_list.get_first())
print()

print("# 7)  Вставка элемента по индексу:")
user_list.insert(2, 67)
print(user_list)
user_list.add_first(6)
print(user_list)
user_list.insert(0, 10)
print(user_list)
print()

print("# 8)  Удаление узла по значению, пусть выдает True, если элемент был удален:")
print("Удаление узла:", user_list.delete_by_data(3))
print(user_list)
print()

print("# 9)  Удаление первого элемента, пусть выдает значение элемента:")
print("Получение значения первого удаленного элемента:", user_list.delete_first())
print(user_list)
print()

print("# 10) Разворот списка за линейное время:")
user_list.reverse()
# Печать списка:
print(user_list)
print()

print("# 11) Копирование списка:")
copy = user_list.copy()
print(copy)
