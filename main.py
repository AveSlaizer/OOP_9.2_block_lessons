from abc import ABC, abstractmethod

# Принципы SOLID
"""
4. Разделение интерфейса - ни один класс не должен зависеть от методов, которые не использует
"""

# Так не правильно
"""
class Deivce(ABC):

    @abstractmethod
    def make_calls(self):
        pass

    @abstractmethod
    def send_sms(self):
        pass

    @abstractmethod
    def connect_internet(self):
        pass


class Smartphone(Deivce):
    pass


class MobilePhone(Deivce):
    pass


class StationaryPhone(Deivce):
    pass
"""


# Правильно так
"""
class CallingDevice(ABC):

    @abstractmethod
    def make_calls(self):
        pass


class MessagingDevice(ABC):

    @abstractmethod
    def send_sms(self):
        pass


class InternetDevice(ABC):

    @abstractmethod
    def connect_internet(self):
        pass


class Smartphone(CallingDevice, MessagingDevice, InternetDevice):

    def make_calls(self):
        pass

    def send_sms(self):
        pass

    def connect_internet(self):
        pass


class MobilePhone(CallingDevice, MessagingDevice):

    def make_calls(self):
        pass

    def send_sms(self):
        pass


class StationaryPhone(CallingDevice):

    def make_calls(self):
        pass
"""

"""
Задача 1. Определить классы для создания устройства, которое может печатать, сканировать, копировать документы
"""



def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
