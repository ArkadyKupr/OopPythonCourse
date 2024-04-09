from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.__side_length = side_length

    @property
    def get_width(self):
        return self.__side_length

    @property
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


class Triangle(Shape):
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2
        self.__x_3 = x_3
        self.__y_3 = y_3

    @property
    def get_width(self):
        return max(self.__x_1, self.__x_2, self.__x_3) - min(self.__x_1, self.__x_2, self.__x_3)

    @property
    def get_height(self):
        return max(self.__y_1, self.__y_2, self.__y_3) - min(self.__y_1, self.__y_2, self.__y_3)

    def be_lying_in_one_line(self):
        epsilon = 1.0e-10

        if abs((self.__y_1 - self.__y_2) * (self.__x_2 - self.__x_3) - (self.__y_2 - self.__y_3) * (
                self.__x_1 - self.__x_2)) < epsilon:
            return True

        return False

    def get_side_length(self, x_1, y_1, x_2, y_2):
        return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

    def get_area(self):
        if Triangle.be_lying_in_one_line(self):
            return 0

        side_a_length = Triangle.get_side_length(self, self.__x_1, self.__y_1, self.__x_2, self.__y_2)
        side_b_length = Triangle.get_side_length(self, self.__x_1, self.__y_1, self.__x_3, self.__y_3)
        side_c_length = Triangle.get_side_length(self, self.__x_2, self.__y_2, self.__x_3, self.__y_3)

        half_perimeter = (side_a_length + side_b_length + side_c_length) / 2
        triangle_area = math.sqrt(
            half_perimeter * (half_perimeter - side_a_length) * (half_perimeter - side_b_length) *
            (half_perimeter - side_c_length))

        return triangle_area

    def get_perimeter(self):
        if Triangle.be_lying_in_one_line(self):
            return 0

        side_a_length = math.sqrt((self.__x_1 - self.__x_2) ** 2 + (self.__y_1 - self.__y_2) ** 2)
        side_b_length = math.sqrt((self.__x_1 - self.__x_3) ** 2 + (self.__y_1 - self.__y_3) ** 2)
        side_c_length = math.sqrt((self.__x_3 - self.__x_2) ** 2 + (self.__y_3 - self.__y_2) ** 2)

        return side_a_length + side_b_length + side_c_length

    def __repr__(self):
        return f"Triangle(({self.__x_1}, {self.__y_1}); ({self.__x_2}, {self.__y_2}); ({self.__x_3}, {self.__y_3})"

    def __hash__(self):
        return hash((self.__x_1, self.__y_1, self.__x_2, self.__y_2, self.__x_3, self.__y_3))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return (self.__x_1 == other.__x_1 and self.__y_1 == other.__y_1 and self.__x_2 == other.__x_2
                and self.__y_2 == other.__y_2 and self.__x_3 == other.__x_3 and self.__y_3 == other.__y_3)


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    @property
    def get_width(self):
        return self.__width

    @property
    def get_height(self):
        return self.__height

    def get_area(self):
        return self.__height * self.__width

    def get_perimeter(self):
        return 2 * (self.__height + self.__width)

    def __repr__(self):
        return f"Rectangle(width: {self.__width}, height: {self.__height})"

    def __hash__(self):
        return hash((self.__width, self.__height))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__width == other.__width and self.__height == other.__height


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def get_width(self):
        return 2 * self.__radius

    @property
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
