from hash_table_task.hash_table import HashTable

user_hash_table = HashTable(4)

user_hash_table[1100] = "tyu"
user_hash_table[1200] = "ty"
user_hash_table[201] = "ty"
user_hash_table[301] = "ty"

print("Проверка __contains__:")
print([1100, "tyu"] in user_hash_table[1100])
print()

print("Проверка __getitem__:")
print(user_hash_table[201][0])
print()

print("Проверка __iter__:")
iterator = iter(user_hash_table)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
