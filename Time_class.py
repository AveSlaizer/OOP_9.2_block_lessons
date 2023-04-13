class Time:
    HOUR = 3600
    MINUTE = 60

    def __init__(self, value: int):
        self.__value = value

    @staticmethod
    def __format(time):
        return f"{time // 10}{time % 10}"

    @classmethod
    def create_time(cls, hours: int, minutes: int, seconds: int):
        # TODO: реализовать метод
        pass

    def __is_time(self, other):
        if not isinstance(other, Time):
            raise TypeError(f"Невозможно выполнить сравнение между типами {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")

    def __str__(self):
        hours = self.__value // Time.HOUR % 24
        minute = self.__value // Time.MINUTE % 60
        second = self.__value % 60
        return f"{Time.__format(hours)}:" \
               f"{Time.__format(minute)}:" \
               f"{Time.__format(second)}"

    def __eq__(self, other):
        self.__is_time(other)
        return self.__value == other.__value

    def __lt__(self, other):
        self.__is_time(other)
        return self.__value < other.__value

    def __le__(self, other):
        self.__is_time(other)
        return self.__value <= other.__value

    def __ne__(self, other):
        self.__is_time(other)
        return self.__value != other.__value

    def __gt__(self, other):
        self.__is_time(other)
        return self.__value > other.__value

    def __ge__(self, other):
        self.__is_time(other)
        return self.__value >= other.__value

    def __hash__(self):
        return hash(self.__value)

    def __add__(self, other):
        if isinstance(other, int):
            t = self.__value + other
            return Time(t)
        if isinstance(other, Time):
            t = self.__value + other.__value
            return Time(t)
        raise TypeError(f"Невозможно выполнить операцию сложения между типами {self.__class__.__name__} и "
                        f"{other.__class__.__name__}")
