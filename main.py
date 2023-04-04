from abc import ABC, abstractmethod
from figures import Rectangle, Circle


"""
Абстрактные классы.
Определяет общий интерфейс для набора подклассов.
Особенности:
1. Содержит абстрактные методы - методы которые не имеют реализации.
2. Нельзя создать экземпляр абстрактного класса.
3. Класс наследник обязан переопределить все методы, которые описаны в абстрактном классе.
"""


def execute_application():
    rect = Rectangle(0, 0, 5, 6)
    print(rect.area())


if __name__ == "__main__":
    execute_application()
