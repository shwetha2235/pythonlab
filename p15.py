""" This program uses Python's abc module to build an abstract geometric framework (ABC) with mandatory
@abstractmethod blueprints. Subclasses like Vector or Circle implement these abstract contracts while
overloading standard mathematical magic dunder methods (__add__, __eq__, __lt__, __str__) to perform
intuitive vector and spatial calculations."""


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __add__(self, other):
        return self.area() + other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return f"Circle Area: {self.area():.2f}"


c1 = Circle(3)
c2 = Circle(4)

print(c1)
print(c2)
print("Combined Area:", round(c1 + c2, 2))
print("Equal Areas:", c1 == c2)
print("First Circle Smaller:", c1 < c2)
