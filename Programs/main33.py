from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculateArea(self):
        return self.width * self.height

circle=Circle(5)
rectangle=Rectangle(4, 6)

print(f"Circle Area: ",circle.calculateArea())
print(f"Rectangle Area: ",rectangle.calculateArea())
