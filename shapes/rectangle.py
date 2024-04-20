from shape import Shape


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def get_width(self):
        return self.__width

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
