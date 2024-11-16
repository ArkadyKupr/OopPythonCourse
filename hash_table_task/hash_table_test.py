from hash_table_task.hash_table import HashTable
from hash_table_task.hash_table_element import HashTableElement


user_hash_table = HashTable(6)

print(user_hash_table)

element_1 = HashTableElement(1100, "tyu")
# Создание списка list - hashable type
element_2 = [1, 2, 4, 5]
# Создание кортежа tuple - hashable type
element_3 = (1, 2, 4, 5)
# Создание словаря dict - unhashable type
element_4 = {1: "A", 2: "B", 3: "C", 5: "D"}
# Создание множества set - unhashable type
element_5 = {1, 2, 4, 5}

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
print()

print("Проверка __getitem__:")
print(user_hash_table[3])
print(user_hash_table[1])
print()

print("Проверка __delitem__:")
print("Хэш-таюлица объектов до удалений:", user_hash_table)
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
