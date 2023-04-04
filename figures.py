from math import pi, sin, sqrt
from abc import ABC, abstractmethod


class Figure:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    #@abstractmethod
    def x(self):
        return self.__x

    @x.setter
    #@abstractmethod
    def x(self, x: int):
        self.__x = x

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class RectangleFormulas(ABC):

    @abstractmethod
    def area_by_diagonal(self):
        pass


class CircleFormulas(ABC):
    pass


# Прямоугольник
class Rectangle(Figure, RectangleFormulas):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    @property
    def diagonal(self):
        return self.diagonal

    @diagonal.setter
    def diagonal(self, d):
        self.diagonal = d

    def area(self):
        return self.__width * self.__height

    def perimetr(self):
        return 2 * (self.__width + self.__height)

    def __diagonal(self):
        return sqrt(self.__width ** 2 + self.__height ** 2)

    def area_by_diagonal(self):
        d = self.__diagonal()
        return self.__width * sqrt(d ** 2 - self.__width ** 2)


# Окружность
class Circle(Figure):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.__radius = radius

    def area(self):
        return pi * self.__radius ** 2

    def perimetr(self):
        return 2 * (pi * self.__radius)
