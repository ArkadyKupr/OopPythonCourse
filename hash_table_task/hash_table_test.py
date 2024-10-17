from hash_table_task.hash_table import HashTable
from hash_table_task.hash_table_element import HashTableElement


user_hash_table = HashTable(5)

print(user_hash_table)

element_1 = HashTableElement(1100, "tyu")
element_2 = HashTableElement(1200, "ty")
element_3 = HashTableElement(201, "ty")
element_4 = HashTableElement(301, "ty")
element_5 = HashTableElement(9001, "ty")

user_hash_table.put_object(element_1)
user_hash_table.put_object(element_2)
user_hash_table.put_object(element_3)
user_hash_table.put_object(element_4)
print(user_hash_table)

print("Проверка __contains__:")
print(element_1 in user_hash_table)
print(element_5 in user_hash_table)
print()

print("Проверка __getitem__:")
print(user_hash_table[3])
print(user_hash_table[1])
print()

print("Проверка __delitem__:")
print("Хэш-таюлица объектов до удалений:", user_hash_table)
print(f"Удаление объекта {element_3}:")
print(user_hash_table.delete_element(element_3))
print(user_hash_table)
print()

print(f"Удаление объекта {element_2}:")
print(user_hash_table.delete_element(element_2))
print(user_hash_table)
print()

print(f"Удаление объекта {element_5}:")
print(user_hash_table.delete_element(element_5))
print()

print("Количество элементов в хэш-таблице:")
print(user_hash_table.elements_quantity)
print()

print("Проверка __iter__:")
iterator = iter(user_hash_table)
print(next(iterator))
print(next(iterator))
