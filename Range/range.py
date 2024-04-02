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

    def get_intersection(self, other):
        if self.__end <= other.__start or other.__end <= self.__start:
            return None
        # один интервал входит в другой
        elif other.__start >= self.__start and other.__end <= self.__end:
            return [other.__start, other.__end]
        elif self.__start >= other.__start and self.__end <= other.__end:
            return [self.__start, self.__end]
        # интервалы пересекаются
        elif self.__start < other.__start:
            return [other.__start, self.__end]
        else:
            return [self.__start, other.__end]

    def get_union(self, other):
        if self.__end < other.__start or other.__end < self.__start:
            return [(self.__start, self.__end), (other.__start, other.__end)]
        # один интервал входит в другой
        elif other.__start >= self.__start and other.__end <= self.__end:
            return [(self.__start, self.__end)]
        elif self.__start >= other.__start and self.__end <= other.__end:
            return [(other.__start, other.__end)]
        # интервалы пересекаются
        elif self.__start < other.__start:
            return [self.__start, other.__end]
        else:
            return [other.__start, self.__end]

    def get_subtraction(self, other):
        if self.__end < other.__start or other.__end < self.__start:
            return [(self.__start, self.__end), (other.__start, other.__end)]
        # один интервал входит в другой
        elif other.__start >= self.__start and other.__end <= self.__end:
            return [(self.__start, other.__start), (other.__end, self.__end)]
        elif self.__start >= other.__start and self.__end <= other.__end:
            return [(other.__start, self.__start), (self.__end, other.__end)]
        # интервалы пересекаются
        elif self.__start < other.__start:
            return [(self.__start, other.__start), (self.__end, other.__end)]
        else:
            return [(other.__start, self.__start), (other.__end, self.__end)]
