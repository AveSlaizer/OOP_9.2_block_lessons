from math import sqrt


class Triangle:

    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def height(self, key: str):
        side = {"a": self.__a, "b": self.__b, "c": self.__c}
        p = 0.5 * (self.__a + self.__b + self.__c)
        return 2 * sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c)) / side[key]

    @staticmethod
    def is_triangle(a: float, b: float, c: float):
        if a < b + c and b < a + c and c < a + b:
            return Triangle(a, b, c)
        else:
            raise Exception("Треугольник с данными торонами не может существовать.")


class Circle:
    pass
