"""    Взаимодействие между классами    """

"""
3 способа взаимодействия между классами:
    1. Наследование.
"""
"""
    2. Ассоциация - это когда один класс включает в себя другой класс в качестве полей.

"""
"""
        2.1 Композиция - это способ, когда объект А не существует отдельно от объекта Б. Объект А создается
        при создании объекта Б.
"""
"""
class Engine:

    def __init__(self, power: int):
        self.__power = power

    @property
    def power(self):
        return self.__power

class Car:

    def __init__(self):
        self.__engine = Engine(100)

    @property
    def engine(self):
        return self.__engine
"""
"""
        2.2 Агрегация - это способ, когда экземпляр класса А создается где-то в другом месте когда и передается 
        параметром в класс Б
        
        Dependency Injection (Внедрение зависимостей) Спсобы внедрения зависимостей:
            1. Через метод инициализации (Через конструктор класса)
            2. Метод установки (сеттер)
            3. Через метод
"""
"""
class Engine:

    def __init__(self, power: int):
        self.__power = power

    @property
    def power(self):
        return self.__power


class Car:

    def __init__(self, engine: Engine):  # Метод инициализации
        self.__engine = engine

    @property
    def engine(self):
        return self.__engine
"""


def execute_application():
    """
    # Композиция
    car = Car()
    print(f"Мощность равно: {car.engine.power}")
    """
    """
    # Агрегация
    engine = Engine(23)
    car = Car(engine)
    print(f"Мощность автомобиля: {car.engine.power}")
    """


if __name__ == "__main__":
    execute_application()
