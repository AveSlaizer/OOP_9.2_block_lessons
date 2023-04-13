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

    def __str__(self):
        hours = self.__value // Time.HOUR % 24
        minute = self.__value // Time.MINUTE % 60
        second = self.__value % 60
        return f"{Time.__format(hours)}:" \
               f"{Time.__format(minute)}:" \
               f"{Time.__format(second)}"
