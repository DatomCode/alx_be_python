import math


class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return f"The area of the Rectangle is: {area}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius ** 2)
        return f"The area of the Circle is: {area}"
