from library_module import *


def execute_application():
    author = Author("Александр", "Пушкин", 1799)
    book = Book("Евгений Онегин", "Роман", author)
    reader = Reader("Анаколий", 23579)

    new_book = Book("Руслан и Валера", "Комедия", author)

    library = Library("им. Осе")


if __name__ == "__main__":
    execute_application()
