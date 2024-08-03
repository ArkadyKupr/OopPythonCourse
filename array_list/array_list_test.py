from array_list import ArrayList

user_array_list = ArrayList(3)

user_array_list[0] = 10
user_array_list[1] = 10
user_array_list[2] = 10
print(user_array_list)

user_array_list.append(2)
print(user_array_list)

user_array_list.ensure_capacity(9)
print(user_array_list)

user_array_list.trim_to_size()

print(user_array_list)

next(user_array_list)
