from array_list_task.array_list import ArrayList

user_array_list_1 = ArrayList(3)

print("Заполнение списка на массиве значениями:")
user_array_list_1[0] = 10
user_array_list_1[1] = 10
user_array_list_1[2] = 10
print(user_array_list_1)
print()

print("Вставка значения в список на массиве:")
user_array_list_1.append(2)
print(user_array_list_1)
print()

print("Удаление значения по индексу. Функция должна возвращать удаленное значение:")
print(user_array_list_1.pop(2))
print(user_array_list_1)
print()

print("Проверка метода trim_to_size:")
user_array_list_1.trim_to_size()
print(user_array_list_1)
print()

print("Проверка метода ensure_capacity:")
user_array_list_1.ensure_capacity(9)
print(user_array_list_1)
print()

user_array_list_2 = ArrayList(1)
user_array_list_2[0] = 10
user_array_list_2.extend([1, 1, 2, 7, 7, 8, 5, 5, 9, 1, 1, 3, 4, 5, 7])
print("Переопределение метода __eq__:", user_array_list_1 == user_array_list_2)
print()

print("Переопределение метода __hash__:", hash(user_array_list_1))
print()

print("Проверка метода extend:")
user_array_list_1.extend([1, 1, 2, 7, 7, 8, 5, 5, 9])
print(user_array_list_1)
print(len(user_array_list_1))
print()

print("Проверка метода copy:")
copied_user_array_list = user_array_list_1.copy()
print(copied_user_array_list)
print()

print("Проверка метода delitem:")
print(user_array_list_1)
del user_array_list_1[-12]
print(user_array_list_1)
print()

print("Проверка метода insert:")
print(user_array_list_1)
user_array_list_1.insert(-1, 10000)
print(user_array_list_1)
print()

print("Список на массиве 1:", user_array_list_1)
print("Список на массиве 2:", user_array_list_2)
user_array_list_1 += user_array_list_2
print("Результат прибавления одного списка на массиве к другому:")
print(user_array_list_1)
print()

user_array_list_1.reverse()
print(user_array_list_1)
print()

print("Реализация класса как итератора")
iterator = iter(user_array_list_1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
