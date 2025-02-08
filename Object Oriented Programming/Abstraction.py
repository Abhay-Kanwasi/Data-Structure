# Abstraction: Only show the details that are necessary of operation not the whole details

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Rectangle")


class Circle(Shape):
    def draw(self):
        print("Circle")


circle = Circle()
circle.draw()

shape = Shape()