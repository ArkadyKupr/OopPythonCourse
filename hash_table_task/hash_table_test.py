from hash_table_task.hash_table import HashTable

user_hash_table = HashTable(100)

user_hash_table[1100] = "tyu"
user_hash_table[1100] = "ty"
user_hash_table[201] = "ty"

print(user_hash_table[1100])

print("tyu" in user_hash_table[1100])
