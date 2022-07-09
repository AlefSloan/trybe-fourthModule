from abc import ABC, abstractmethod
import math


class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimetro(self):
        raise NotImplementedError


class Square(FiguraGeometrica):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimetro(self):
        return self.side * 4


class Rectangle(FiguraGeometrica):
    def __init__(self, heigth, width):
        self.height = heigth
        self.width = width

    def area(self):
        return self.height * self.width

    def perimetro(self):
        return self.height * 2 + self.width * 2


class Circle(FiguraGeometrica):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radius
