"""
Наследование.
1. Позволяет выделить общие характеристики для нескольких классов
2. Позволяет избежать повторения кода при определении классов
3. Один из принципов ООП

Базоаые (родительские) классы
Производные (дочерние) классы
"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        print(f"Класс: {self.__class__.__name__}\n"
              f"Имя: {self.__name}\n"
              f"Возраст: {self.__age}")


class Employee(Person):

    def __init__(self, name: str, age: int, position: str, salary: float):
        super().__init__(name, age)
        self.__position = position
        self.__salary = salary

    def info(self):
        super().info()
        print(f"Должность: {self.__position}\n"
              f"Зарплата: {self.__salary}")


class Programmer(Employee):
    def __init__(self, name: str, age: int, position: str, salary: float, language: str, level: str):
        super().__init__(name, age, position, salary)
        self.__language = language
        self.__level = level

    def info(self):
        super().info()
        print(f"Язык: {self.__language}\n"
              f"Уровень: {self.__level}\n")


def execute_application():
    person = Person("Вася", 23)
    person.info()
    print()

    employee = Employee("Юра", 32, "Менеджер", 12312)
    employee.info()
    print()

    programmer = Programmer("Миша", 13, "Programmer", 123456, "Go", "Junior")
    programmer.info()


if __name__ == "__main__":
    execute_application()
