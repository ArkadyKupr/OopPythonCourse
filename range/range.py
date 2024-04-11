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
        if ((self.__end <= other.__start) or
                (self.__start >= other.__end)):
            return None
        # один интервал входит в другой
        else:
            return [Range(max(other.__start, self.__start), min(self.__end, other.__end))]

    def get_union(self, other):
        if self.__end < other.__start or other.__end < self.__start:
            return [Range(self.__start, self.__end), Range(other.__start, other.__end)]
        # один интервал входит в другой
        else:
            return [Range(min(other.__start, self.__start), max(self.__end, other.__end))]

    def get_difference(self, other):
        if ((self.__start <= other.__start and self.__end <= other.__start) or
                (self.__start >= other.__end and self.__end >= other.__end)):
            return [Range(self.__start, self.__end)]

        elif self.__start <= other.__start and self.__end <= other.__end:
            if self.__start == other.__start:
                return []
            else:
                return [Range(self.__start, other.__start)]

        elif self.__start >= other.__start and self.__end >= other.__end:
            if self.__end == other.__end:
                return []

            else:
                return [Range(other.__end, self.__end)]

        return [Range(self.__start, other.__start), Range(other.__end, self.__end)]

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, number):
        return self.__start <= number <= self.__end
