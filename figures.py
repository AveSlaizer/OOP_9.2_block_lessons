from math import pi
from abc import ABC, abstractmethod


class Figure:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


# Прямоугольник
class Rectangle(Figure):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    #def area(self):
     #   return self.__width * self.__height

    def perimetr(self):
        return 2 * (self.__width + self.__height)


# Окружность
class Circle(Figure):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.__radius = radius

    def area(self):
        return pi * self.__radius ** 2

    def perimetr(self):
        return 2 * (pi * self.__radius)
