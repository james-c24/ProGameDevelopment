class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("Area of the circle is",(self.radius**2*3.14)+"cm^2.")

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        print("Area of the rectangle is",(self.height*self.width)+"cm^2.")

c = Circle(5)
r = Rectangle(3,6)
shapes = [c,r]

for shape in shapes:
    shape.area()
