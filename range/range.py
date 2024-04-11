class Range:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    def __repr__(self):
        return f"({self.__start}; {self.__end})"

    def get_intersection(self, other):
        if self.__end <= other.__start or other.__end <= self.__start:
            return []
        # один интервал входит в другой
        elif other.__start >= self.__start and other.__end <= self.__end:
            return Range(other.__start, other.__end)
        elif self.__start >= other.__start and self.__end <= other.__end:
            return Range(self.__start, self.__end)
        # интервалы пересекаются
        elif self.__start < other.__start:
            return Range(other.__start, self.__end)
        else:
            return Range(self.__start, other.__end)

    def get_union(self, other):
        if self.__end < other.__start or other.__end < self.__start:
            return Range(self.__start, self.__end), Range(other.__start, other.__end)
        # один интервал входит в другой
        elif other.__start >= self.__start and other.__end <= self.__end:
            return Range(self.__start, self.__end)
        elif self.__start >= other.__start and self.__end <= other.__end:
            return Range(other.__start, other.__end)
        # интервалы пересекаются
        elif self.__start < other.__start:
            return Range(self.__start, other.__end)
        else:
            return Range(other.__start, self.__end)

    def get_subtraction(self, other):
        if self.__start == other.__start and self.__end == other.__end:
            return []
        elif self.__end < other.__start or other.__end < self.__start:
            return Range(self.__start, self.__end), Range(other.__start, other.__end)
        # один интервал входит в другой
        elif other.__start >= self.__start and other.__end <= self.__end:
            return Range(self.__start, other.__start), Range(other.__end, self.__end)
        elif self.__start >= other.__start and self.__end <= other.__end:
            return Range(other.__start, self.__start), Range(self.__end, other.__end)
        # интервалы пересекаются
        elif self.__start < other.__start:
            return Range(self.__start, other.__start), Range(self.__end, other.__end)
        else:
            return Range(other.__start, self.__start), Range(other.__end, self.__end)

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, number):
        return self.__start <= number <= self.__end

