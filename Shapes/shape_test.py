from shapes import Circle, Rectangle, Triangle, Square

shapes = [Circle(10),
          Rectangle(5, 10),
          Triangle(5, 9, 5, 9, 5, 9),
          Square(5), Square(15)]

for s in shapes:
    [].append((s.get_area(), s))


print("Фигура с максимальной площадью:", sorted(shapes, key=lambda x: x.get_area(), reverse=True)[0])
print("Фигура со вторым по величине периметром:", sorted(shapes, key=lambda x: x.get_perimeter(), reverse=True)[1])
