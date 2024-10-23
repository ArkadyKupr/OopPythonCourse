from vector_task.vector import Vector

vector_1 = Vector([1, 2, 3, 0])
vector_2 = Vector([1, 2, 3])

vector_3 = Vector(2)
print("a:", vector_3)

vector_4 = Vector(7, [1, 2, 9, 8])
print("d:", vector_4)

print("Свойство для получения длины вектора:", vector_4.get_length())
print("Свойство для получения размерности вектора:", vector_4.dimension)

print("Реализация метода __repr__:", vector_1)

print("Переопределение метода __eq__:", vector_1 == vector_2)

print("Переопределение метода __hash__:", hash(vector_1))

vector_2 += vector_1
print("Прибавление к вектору другого вектора:", vector_2)

vector_2 -= vector_1
print("Вычитание из вектора другого вектора:", vector_2)

vector_1 = Vector([1, 2, 3, 0])
vector_2 = Vector([1, 2, 4, 0, 0])
print("Сложение двух векторов с созданием нового:", vector_1 + vector_2)
print("Вычитание двух векторов с созданием нового:", vector_1 - vector_2)

vector_1 = Vector([1, 2, 100, 3])
vector_1 *= -1
print("Умножение вектора на скаляр:", vector_1)

print("Получение компоненты вектора по индексу:", vector_1[3])

vector_1[-3] = 100
print("Установка компоненты вектора по индексу:", vector_1)

print("Разворот вектора:", vector_1.reverse())

print("Вектор:", vector_1)
print("Вектор:", vector_2)

vector_5 = Vector([1, 9, 0, 10])
vector_6 = Vector([1, 3, 7])
print("Скалярное произведение векторов:", Vector.get_scalar_product(vector_5, vector_6))

print("Поддержка slice в __getitem__:")
print("Вектор:", vector_5)
user_list = [1, 9, 0, 10]
print()

print(vector_5[::])
print("Работа slice на списке:", user_list[::])
print()

print(vector_5[1:2:1])
print("Работа slice на списке:", user_list[1:2:1])
print()

print(vector_5[1:3:-1])
print("Работа slice на списке:", user_list[1:3:-1])
print()

print(vector_5[-4:-1:-2])
print("Работа slice на списке:", user_list[-4:-1:-2])
print()

print(vector_5[-3:-1:2])
print("Работа slice на списке:", user_list[-3:-1:2])
print()

print(vector_5[:-1:2])
print("Работа slice на списке:", user_list[:-1:2])
print()
