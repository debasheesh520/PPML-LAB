class Shape:
    def __init__(self):
        print("This is a shape")

class Rectangle(Shape):
    def __init__(self, l, b):
        super().__init__()
        self.length = l
        self.breadth = b

    def area(self):
        a = self.length * self.breadth
        print("Area of Rectangle:", a)

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.radius = r

    def area(self):
        a = 3.14 * self.radius * self.radius
        print("Area of Circle:", a)

r1 = Rectangle(5, 4)
c1 = Circle(3)

r1.area()
c1.area()
