from range import Range


def test(numbers_range_1, numbers_range_2):
    print(f"Интервал-пересечение двух интервалов {numbers_range_1} и {numbers_range_2}:",
          numbers_range_1.get_intersection(numbers_range_2))
    print(f"Объединение двух интервалов {numbers_range_1} и {numbers_range_2}:",
          numbers_range_1.get_union(numbers_range_2))
    print(f"Разность двух интервалов {numbers_range_1} и {numbers_range_2}:",
          numbers_range_1.get_difference(numbers_range_2))
    print()


test(Range(1, 10), Range(10, 20))

test(Range(10, 20), Range(1, 10))

test(Range(10, 13), Range(11, 15))

test(Range(10, 15), Range(11, 13))

test(Range(11, 15), Range(14, 119))

test(Range(14, 119), Range(11, 15))

test(Range(1, 7), Range(1, 5))

numbers_range = Range(13, 18)

number_in_range = int(input("Введите число: "))
line = f"Число {number_in_range} входит в диапазон {numbers_range}:"
print(line, numbers_range.is_inside(number_in_range))

print(f"Длина диапазона {numbers_range}:", numbers_range.get_length())
