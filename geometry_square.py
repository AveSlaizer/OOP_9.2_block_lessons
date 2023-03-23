from math import sin


"""
Создайте класс для подсчета площади геометрических фигур. 
Класс должен предоставлять функциональность для подсчета площади треугольника по разным формулам,
площади прямоугольника, площади квадрата,  площади ромба. Расчеты реализовать через статические методы
"""


class GeometrySquare:

    @staticmethod
    def triangle_square_1(a: float, h: float):
        return 0.5 * a * h

    @staticmethod
    def triangle_square_2(a: float, b: float, angle: int):
        return 0.5 * a * b * sin(angle)

    @staticmethod
    def triangle_square_3(a: float, angle_a: int, angle_b: int):
        return 0.5 * a * a * (sin(angle_a) * sin(angle_b)) * sin(angle_a + angle_b)