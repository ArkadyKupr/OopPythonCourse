class Range:
    def __init__(self, start_1, end_1, start_2, end_2):
        self.__start_1 = start_1
        self.__end_1 = end_1
        self.__start_2 = start_2
        self.__end_2 = end_2

    @property
    def start_1(self):
        return self.__start_1

    @start_1.setter
    def start_1(self, start_1):
        self.__start_1 = start_1

    @property
    def end_1(self):
        return self.__end_1

    @end_1.setter
    def end_1(self, end_1):
        self.__end_1 = end_1

    @property
    def start_2(self):
        return self.__start_2

    @start_2.setter
    def start_2(self, start_2):
        self.__start_2 = start_2

    @property
    def end_2(self):
        return self.__end_2

    @end_2.setter
    def end_2(self, end_2):
        self.__end_2 = end_2

    def get_intersection_range(self):
        if self.__end_1 <= self.__start_2 or self.__end_2 <= self.__start_1:
            return None
        # один интервал входит в другой
        elif self.__start_2 >= self.__start_1 and self.__end_2 <= self.__end_1:
            return [self.__start_2, self.__end_2]
        elif self.__start_1 >= self.__start_2 and self.__end_1 <= self.__end_2:
            return [self.__start_1, self.__end_1]
        # интервалы пересекаются
        elif self.__start_1 < self.__start_2:
            return [self.__start_2, self.__end_1]
        else:
            return [self.__start_1, self.__end_2]

    def get_merged_range(self):
        if self.__end_1 < self.__start_2 or self.__end_2 < self.__start_1:
            return [(self.__start_1, self.__end_1), (self.__start_2, self.__end_2)]
        # один интервал входит в другой
        elif self.__start_2 >= self.__start_1 and self.__end_2 <= self.__end_1:
            return [(self.__start_1, self.__end_1)]
        elif self.__start_1 >= self.__start_2 and self.__end_1 <= self.__end_2:
            return [(self.__start_2, self.__end_2)]
        # интервалы пересекаются
        elif self.__start_1 < self.__start_2:
            return [self.__start_1, self.__end_2]
        else:
            return [self.__start_2, self.__end_1]

    def get_subtracted_range(self):
        if self.__end_1 < self.__start_2 or self.__end_2 < self.__start_1:
            return [(self.__start_1, self.__end_1), (self.__start_2, self.__end_2)]
        # один интервал входит в другой
        elif self.__start_2 >= self.__start_1 and self.__end_2 <= self.__end_1:
            return [(self.__start_1, self.__start_2), (self.__end_2, self.__end_1)]
        elif self.__start_1 >= self.__start_2 and self.__end_1 <= self.__end_2:
            return [(self.__start_2, self.__start_1), (self.__end_1, self.__end_2)]
        # интервалы пересекаются
        elif self.__start_1 < self.__start_2:
            return [(self.__start_1, self.__start_2), (self.__end_1, self.__end_2)]
        else:
            return [(self.__start_2, self.__start_1), (self.__end_2, self.__end_1)]


numbers_ranges = Range(1, 10, 10, 20)
print("Интервал-пересечение двух интервалов:", numbers_ranges.get_intersection_range())
print("Объединение двух интервалов:", numbers_ranges.get_merged_range())
print("Разность двух интервалов:", numbers_ranges.get_subtracted_range())

numbers_ranges = Range(10, 20, 1, 10)
print("Интервал-пересечение двух интервалов:", numbers_ranges.get_intersection_range())
print("Объединение двух интервалов:", numbers_ranges.get_merged_range())
print("Разность двух интервалов:", numbers_ranges.get_subtracted_range())

numbers_ranges = Range(10, 13, 11, 15)
print("Интервал-пересечение двух интервалов:", numbers_ranges.get_intersection_range())
print("Объединение двух интервалов:", numbers_ranges.get_merged_range())
print("Разность двух интервалов:", numbers_ranges.get_subtracted_range())

numbers_ranges = Range(10, 15, 11, 13)
print("Интервал-пересечение двух интервалов:", numbers_ranges.get_intersection_range())
print("Объединение двух интервалов:", numbers_ranges.get_merged_range())
print("Разность двух интервалов:", numbers_ranges.get_subtracted_range())

numbers_ranges = Range(11, 15, 14, 119)
print("Интервал-пересечение двух интервалов:", numbers_ranges.get_intersection_range())
print("Объединение двух интервалов:", numbers_ranges.get_merged_range())
print("Разность двух интервалов:", numbers_ranges.get_subtracted_range())

numbers_ranges = Range(14, 119, 11, 15)
print("Интервал-пересечение двух интервалов:", numbers_ranges.get_intersection_range())
print("Объединение двух интервалов:", numbers_ranges.get_merged_range())
print("Разность двух интервалов:", numbers_ranges.get_subtracted_range())
