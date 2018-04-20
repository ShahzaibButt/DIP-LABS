class Shape:
    @staticmethod
    def printType():
        print("Shape")
    def draw(self):
        print("Draw")
    def area(self):
        print("Area")


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def draw(self):
        print("Rectangle draw")
    def area(self):
        print("Rectangle area")

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = 0
        self.b = 0
        self.c = 0
    def draw(self):
        print("Triangle draw")
    def area(self):
        print("Triangle Area")

Shape.printType()
sh = Shape()
sh.area()
sh.draw()

rec = Rectangle(3,4)
rec.draw()
rec.area()

tri = Triangle(2,2,2)
tri.draw()
tri.area()