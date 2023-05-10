from rectangle2 import Rectangle, Square, Circle

r1 = Rectangle(3, 4)
r2 = Rectangle(12, 5)

print(r1.get_area())
print(r2.get_area())

sq1 = Square(5)
sq2 = Square(10)

print(sq1.get_area_square(),
      sq2.get_area_square())

cir1 = Circle(5)
cir2 = Circle(10)

print(cir1.get_area_circle(),
      cir2.get_area_circle())

figures = [r1, r2, sq1, sq2, cir1, cir2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())