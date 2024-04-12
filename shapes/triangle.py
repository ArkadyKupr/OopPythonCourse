from shapes import Shape
import math


class Triangle(Shape):
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2
        self.__x_3 = x_3
        self.__y_3 = y_3

    @property
    def x_1(self):
        return self.__x_1

    @property
    def y_1(self):
        return self.__y_1

    @property
    def x_2(self):
        return self.__x_2

    @property
    def y_2(self):
        return self.__y_2

    @property
    def x_3(self):
        return self.__x_3

    @property
    def y_3(self):
        return self.__y_3

    def get_width(self):
        return max(self.__x_1, self.__x_2, self.__x_3) - min(self.__x_1, self.__x_2, self.__x_3)

    def get_height(self):
        return max(self.__y_1, self.__y_2, self.__y_3) - min(self.__y_1, self.__y_2, self.__y_3)

    def __lie_on_same_line(self):
        epsilon = 1.0e-10

        return abs((self.__y_1 - self.__y_2) * (self.__x_2 - self.__x_3) - (self.__y_2 - self.__y_3) * (
                self.__x_1 - self.__x_2)) < epsilon

    @staticmethod
    def __get_side_length(x_1, y_1, x_2, y_2):
        return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

    def get_area(self):
        if self.__lie_on_same_line():
            return 0

        side_a_length = self.__get_side_length(self.__x_1, self.__y_1, self.__x_2, self.__y_2)
        side_b_length = self.__get_side_length(self.__x_1, self.__y_1, self.__x_3, self.__y_3)
        side_c_length = self.__get_side_length(self.__x_2, self.__y_2, self.__x_3, self.__y_3)

        half_perimeter = (side_a_length + side_b_length + side_c_length) / 2
        triangle_area = math.sqrt(
            half_perimeter * (half_perimeter - side_a_length) * (half_perimeter - side_b_length) *
            (half_perimeter - side_c_length))

        return triangle_area

    def get_perimeter(self):
        side_a_length = self.__get_side_length(self.__x_1, self.__y_1, self.__x_2, self.__y_2)
        side_b_length = self.__get_side_length(self.__x_1, self.__y_1, self.__x_3, self.__y_3)
        side_c_length = self.__get_side_length(self.__x_2, self.__y_2, self.__x_3, self.__y_3)

        if self.__lie_on_same_line():
            return max(side_a_length, side_b_length, side_c_length)

        return side_a_length + side_b_length + side_c_length

    def __repr__(self):
        return f"Triangle(({self.__x_1}, {self.__y_1}); ({self.__x_2}, {self.__y_2}); ({self.__x_3}, {self.__y_3}))"

    def __hash__(self):
        return hash((self.__x_1, self.__y_1, self.__x_2, self.__y_2, self.__x_3, self.__y_3))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return (self.__x_1 == other.__x_1 and self.__y_1 == other.__y_1 and self.__x_2 == other.__x_2
                and self.__y_2 == other.__y_2 and self.__x_3 == other.__x_3 and self.__y_3 == other.__y_3)
