from range import Range


numbers_range_1 = Range(1, 10)
number_range_2 = Range(10, 20)
print("Интервал-пересечение двух интервалов:", numbers_range_1.get_intersection(number_range_2))
print("Объединение двух интервалов:", numbers_range_1.get_union(number_range_2))
print("Разность двух интервалов:", numbers_range_1.get_subtraction(number_range_2))

numbers_range_3 = Range(10, 20)
numbers_range_4 = Range(1, 10)
print("Интервал-пересечение двух интервалов:", numbers_range_3.get_intersection(numbers_range_4))
print("Объединение двух интервалов:", numbers_range_3.get_union(numbers_range_4))
print("Разность двух интервалов:", numbers_range_3.get_subtraction(numbers_range_4))

numbers_range_5 = Range(10, 13)
numbers_range_6 = Range(11, 15)
print("Интервал-пересечение двух интервалов:", numbers_range_5.get_intersection(numbers_range_6))
print("Объединение двух интервалов:", numbers_range_5.get_union(numbers_range_6))
print("Разность двух интервалов:", numbers_range_5.get_subtraction(numbers_range_6))

numbers_range_7 = Range(10, 15)
numbers_range_8 = Range(11, 13)
print("Интервал-пересечение двух интервалов:", numbers_range_7.get_intersection(numbers_range_8))
print("Объединение двух интервалов:", numbers_range_7.get_union(numbers_range_8))
print("Разность двух интервалов:", numbers_range_7.get_subtraction(numbers_range_8))

numbers_range_9 = Range(11, 15)
numbers_range_10 = Range(14, 119)
print("Интервал-пересечение двух интервалов:", numbers_range_9.get_intersection(numbers_range_10))
print("Объединение двух интервалов:", numbers_range_9.get_union(numbers_range_10))
print("Разность двух интервалов:", numbers_range_9.get_subtraction(numbers_range_10))

numbers_range_11 = Range(14, 119)
numbers_range_12 = Range(11, 15)
print("Интервал-пересечение двух интервалов:", numbers_range_11.get_intersection(numbers_range_12))
print("Объединение двух интервалов:", numbers_range_11.get_union(numbers_range_12))
print("Разность двух интервалов:", numbers_range_11.get_subtraction(numbers_range_12))
