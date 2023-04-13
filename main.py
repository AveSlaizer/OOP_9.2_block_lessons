from Time_class import Time


def execute_application():
    time = Time(10)
    time2 = Time(186500)
    print(time)
    print(time == time2)
    time -= 86400
    print(time)


if __name__ == "__main__":
    execute_application()
