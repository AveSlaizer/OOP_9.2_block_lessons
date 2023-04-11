from abc import ABC, abstractmethod
from MagicMethods import Point

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
"""
class PrintingDevice(ABC):

    @abstractmethod
    def print_document(self):
        pass

class ScanningDevice(ABC):

    @abstractmethod
    def scan_document(self):
        pass

class CopingDevice(ABC):

    @abstractmethod
    def copy_document(self):
        pass

class Printer(PrintingDevice):

    def print_document(self):
        # печать документа
        pass

class Scaner(ScanningDevice):

    def scan_document(self):
        # сканирование документа
        pass

class MFD(ScanningDevice, PrintingDevice, CopingDevice):

    def print_document(self):
        # печать документа
        pass

    def scan_document(self):
        # сканирование документа
        pass

    def copy_document(self):
        # компирование документа
        pass
"""


def execute_application():
    point1 = Point(1, 2)
    point2 = Point(1, 2)
    print(hash(point1))
    print(hash(point2))
    print(point1 == point2)


if __name__ == "__main__":
    execute_application()
