from vector import Vector


user_vector = Vector([1, 2, 3])
user_vector_1 = Vector([1, 2, 3])

user_vector_2 = Vector(2)
print("a:", user_vector_2)

user_vector_3 = Vector(7, [1, 2, 5, 8])
print("d:", user_vector_3)

print("Свойство для получения длины вектора:", user_vector_3.get_length())
print("Свойство для получения размерности вектора:", user_vector_3.dimension)

print("Реализация метода _repr_:", user_vector)

print("Переопределение метода __eq__:", user_vector == user_vector_1)

print("Прибавление к вектору другого вектора:", user_vector_1.get_sum_vector(user_vector))
print("Вычитание из вектора другого вектора:", user_vector.get_diff_vector(user_vector_1))

user_vector = Vector([1, 2, 3])
user_vector_1 = Vector([1, 2, 4])
print("Сложение двух векторов с созданием нового:", user_vector.get_sum_new_vector(user_vector_1))
print("Вычитание двух векторов с созданием нового:", user_vector.get_difference_new_vector(user_vector_1))

user_vector = Vector([1, 2, 100, 3])
print("Умножение вектора на скаляр:", user_vector.get_multiplied_vector(2))

print("Установка компоненты вектора по индексу:", user_vector.change_vector_component(1, 100))

print("Разворот вектора:", user_vector.get_reverse_vector())

print("Вектор:", user_vector)
print("Вектор:", user_vector_1)

print("Скалярное произведение векторов:", user_vector.scalar_multiplicate_vectors(user_vector_1))
