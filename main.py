"""
Наследование.
1. Позволяет выделить общие характеристики для нескольких классов
2. Позволяет избежать повторения кода при определении классов
3. Один из принципов ООП
"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


class Programmer:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
