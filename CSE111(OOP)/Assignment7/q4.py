# question4

import math


class Circle:
    def __init__(self, n1):
        self.__radius = n1

    def setRadius(self):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi*self.__radius**2

    def __add__(self, n2):
        new_radius = self.__radius + n2.__radius
        object = Circle(new_radius)
        return object


c1 = Circle(4)
print("First circle radius:", c1.getRadius())
print("First circle area:", c1.area())
c2 = Circle(5)
print("Second circle radius:", c2.getRadius())
print("Second circle area:", c2.area())
c3 = c1 + c2
print("Third circle radius:", c3.getRadius())
print("Third circle area:", c3.area())
