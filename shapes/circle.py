from shapes import Shape
import math


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def get_width(self):
        return 2 * self.__radius

    def get_height(self):
        return 2 * self.__radius

    def get_area(self):
        return math.pi * self.__radius * self.__radius

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    def __repr__(self):
        return f"Circle(radius: {self.__radius})"

    def __hash__(self):
        return hash(self.__radius)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__radius == other.__radius
