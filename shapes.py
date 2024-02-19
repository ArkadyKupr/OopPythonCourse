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


    def get_width(self):
        return self.__side_length


    def get_height(self):
        return self.__side_length


    def get_area(self):
        return self.__side_length * self.__side_length


    def get_perimeter(self):
        return 4 * self.__side_length


class Triangle(Shape):
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2
        self.__x_3 = x_3
        self.__y_3 = y_3


    def get_width(self):
        return max(self.__x_1, self.__x_2, self.__x_3) - min(self.__x_1, self.__x_2, self.__x_3)


    def get_height(self):
        return max(self.__y_1, self.__y_2, self.__y_3) - min(self.__y_1, self.__y_2, self.__y_3)


    def get_area(self):
        EPSILON = 1.0e-10

        if abs((self.__y_1 - self.__y_2) * (self.__x_2 - self.__x_3) - (self.__y_2 - self.__y_3) * (self.__x_1 - self.__x_2)) < EPSILON:
            return "Точки лежат на одной прямой"

        side_a_length = math.sqrt((self.__x_1 - self.__x_2) ** 2 + (self.__y_1 - self.__y_2) ** 2)
        side_b_length = math.sqrt((self.__x_1 - self.__x_3) ** 2 + (self.__y_1 - self.__y_3) ** 2)
        side_c_length = math.sqrt((self.__x_3 - self.__x_2) ** 2 + (self.__y_3 - self.__y_2) ** 2)

        half_perimeter = (side_a_length + side_b_length + side_c_length) / 2
        triangle_area = math.sqrt(
            half_perimeter * (half_perimeter - side_a_length) * (half_perimeter - side_b_length) *
            (half_perimeter - side_c_length))

        return triangle_area


    def get_perimeter(self):
        EPSILON = 1.0e-10

        if abs((self.__y_1 - self.__y_2) * (self.__x_2 - self.__x_3) - (self.__y_2 - self.__y_3) * (
                self.__x_1 - self.__x_2)) < EPSILON:
            return "Точки лежат на одной прямой"

        side_a_length = math.sqrt((self.__x_1 - self.__x_2) ** 2 + (self.__y_1 - self.__y_2) ** 2)
        side_b_length = math.sqrt((self.__x_1 - self.__x_3) ** 2 + (self.__y_1 - self.__y_3) ** 2)
        side_c_length = math.sqrt((self.__x_3 - self.__x_2) ** 2 + (self.__y_3 - self.__y_2) ** 2)

        perimeter = side_a_length + side_b_length + side_c_length
        return perimeter


class Rectangle(Shape):
    def __init__(self, rectangle_length, rectangle_width):
        self.__rectangle_length = rectangle_length
        self.__rectangle_width = rectangle_width


    def get_width(self):
        return max(self.__rectangle_width, self.__rectangle_length)


    def get_height(self):
        return min(self.__rectangle_width, self.__rectangle_length)


    def get_length(self):
        return self.__rectangle_length


    def get_area(self):
        return self.__rectangle_length * self.__rectangle_width


    def get_perimeter(self):
        return 2 * (self.__rectangle_length + self.__rectangle_width)


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius


    def get_width(self):
        return 2 * self.__radius


    def get_height(self):
        return 2 * self.__radius


    def get_length(self):
        return 2 * self.__radius


    def get_area(self):
        return math.pi * self.__radius * self.__radius


    def get_perimeter(self):
        return 2 * math.pi * self.__radius


square = Square(5)
print("Длина квадрата:", square.get_width())
print("Высота квадрата:", square.get_height())
print("Площадь квадрата:", square.get_area())
print("Периметр квадрата:", square.get_perimeter())
print()

triangle = Triangle(5, 9, 0, 8, 7, 13)
print("Длина треугольника:", triangle.get_width())
print("Высота треугольника:", triangle.get_height())
print("Площадь треугольника:", triangle.get_area())
print("Периметр треугольника:", triangle.get_perimeter())
print()

rectangle = Rectangle(5, 10)
print("Длина прямоугольника:", rectangle.get_width())
print("Высота прямоугольника:", rectangle.get_height())
print("Площадь прямоугольника:", rectangle.get_area())
print("Периметр прямоугольника:", rectangle.get_perimeter())
print()

circle = Circle(10)
print("Длина круга:", circle.get_width())
print("Высота круга:", circle.get_height())
print("Площадь круга:", circle.get_area())
print("Длина окружности:", circle.get_perimeter())
