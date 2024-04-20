from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from square import Square

shapes = [
    Circle(10),
    Rectangle(5, 10),
    Triangle(5, 9, 5, 9, 5, 9),
    Square(5),
    Square(15)
]

print("Фигура с максимальной площадью:", sorted(shapes, key=lambda x: x.get_area(), reverse=True)[0])
print("Фигура со вторым по величине периметром:", sorted(shapes, key=lambda x: x.get_perimeter(), reverse=True)[1])
