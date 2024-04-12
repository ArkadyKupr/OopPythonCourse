from shapes import Shape


class Square(Shape):
    def __init__(self, side_length):
        self.__side_length = side_length

    @property
    def side_length(self):
        return self.__side_length

    def get_width(self):
        return self.__side_length

    def get_height(self):
        return self.__side_length

    def get_area(self):
        return self.__side_length * self.__side_length

    def get_perimeter(self):
        return 4 * self.__side_length

    def __repr__(self):
        return f"Square(side_length: {self.__side_length})"

    def __hash__(self):
        return hash(self.__side_length)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__side_length == other.__side_length
