""" Принципы проектирования классов SOLID """
"""
1. Принцип единственной ответственности - у каждого класса только одна ответственность и он не должен брать 
    другие ответственности

2. Класс должен быть открыт для расширения, но закрыт для изменения
"""


class Radio:

    def __init__(self, station: str):
        self.__station = station

    def play(self):
        return f"В эфире радио {self.__station}"


class MixinRadio:

    def play_radio(self, radio: Radio):
        print(radio.play())


class Power:
    LOWER = 100
    MEDIUM = 150
    UPPER = 200


class Car(MixinRadio):
    """Хранит данные о конкретном автомобиле"""

    def __init__(self, brand: str, year: int, color: str, power: float):
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__power = power

    def __str__(self):
        return f"Марка {self.__brand}, год {self.__year}, цвет {self.__color}"


class FileManagementCar:

    @staticmethod
    def save(car: Car, path: str):
        pass

    @staticmethod
    def load(path: str):
        pass


class DBManagementCar:

    @staticmethod
    def save(car: Car, name: str):
        pass

    @staticmethod
    def load(name: str) -> Car:
        pass


class MobilePhone(MixinRadio):

    def __init__(self, brand: str, year: int, color: str):
        self.__brand = brand
        self.__year = year
        self.__color = color


def execute_application():
    car = Car("BMW", 2005, "pink")
    radio = Radio("Шансон")
    car.play_radio(radio)


if __name__ == "__main__":
    execute_application()
