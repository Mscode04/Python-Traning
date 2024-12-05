from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

    @abstractmethod
    def calculatePerimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius ** 2

    def calculatePerimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculateArea(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calculatePerimeter(self):
        return self.a + self.b + self.c

circle = Circle(5)  # Circle with radius 5
print("Circle Area:", circle.calculateArea())
print("Circle Perimeter:", circle.calculatePerimeter())
triangle = Triangle(3, 4, 5)
print("Triangle Area:", triangle.calculateArea())
print("Triangle Perimeter:", triangle.calculatePerimeter())