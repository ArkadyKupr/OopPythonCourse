from array_list_task.array_list import ArrayList

user_array_list = ArrayList(3)

user_array_list[0] = 10
user_array_list[1] = 10
user_array_list[2] = 10
print(user_array_list)

user_array_list.append(2)
print(user_array_list)

# проверка метода ensure_capacity
user_array_list.ensure_capacity(9)
print(user_array_list)

# проверка метода trim_to_size
user_array_list.trim_to_size()
print(user_array_list)

# реализация класса как итератора
iterator = iter(user_array_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# проверка метода extend
user_array_list.extend([1, 1, 2])
