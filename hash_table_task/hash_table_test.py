from hash_table_task.hash_table import HashTable


user_hash_table = HashTable(6)

print(user_hash_table)

# Создание списка list - hashable type
element_1 = "аргонавт"
# Создание списка list - hashable type
element_2 = tuple[1, 2, 4, 5]
# Создание кортежа tuple - hashable type
element_3 = (1, 2, 4, 5)
# Создание словаря dict - unhashable type
element_4 = tuple({1: "A", 2: "B", 3: "C", 5: "D"})
# Создание множества set - unhashable type
element_5 = tuple({1, 2, 4, 5})

user_hash_table.insert_element(element_1)
user_hash_table.insert_element(element_2)
user_hash_table.insert_element(element_3)
user_hash_table.insert_element(element_4)
user_hash_table.insert_element(element_5)
print(user_hash_table)

print("Проверка __contains__:")
print(f"Элемент {element_1} содержится в хэш-таблице:")
print(element_1 in user_hash_table)
print(f"Элемент {element_4} содержится в хэш-таблице:")
print(element_4 in user_hash_table)
print(f"Элемент {element_5} содержится в хэш-таблице:")
print(element_5 in user_hash_table)
print(f"Элемент None содержится в хэш-таблице:")
print(None in user_hash_table)
print()

print("Проверка __delitem__:")
print("Хэш-таблица объектов до удалений:", user_hash_table)
print(f"Удаление объекта {element_3}:")
print(user_hash_table.delete(element_3))
print(user_hash_table)
print()

print(f"Удаление объекта {element_2}:")
print(user_hash_table.delete(element_2))
print(user_hash_table)
print()

print(f"Удаление объекта {element_5}:")
print(user_hash_table.delete(element_5))
print()

print("Количество элементов в хэш-таблице:")
print(len(user_hash_table))
print()

print("Проверка __iter__:")
iterator = iter(user_hash_table)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
