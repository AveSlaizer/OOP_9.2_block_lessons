from library_module import *


def execute_application():
    author = Author("Александр", "Пушкин", 1799)
    book = Book("Евгений Онегин", "Роман", author)
    reader = Reader("Анаколий", 23579)

    new_book = Book("Руслан и Валера", "Роман", author)

    library = Library("им. Осе")
    library.add_book(book)
    library.add_book(new_book)

    list_books = GenreFilterBooksLibrary.get_books(library, "Роман")

    for book in list_books:
        print(book)

    book_list = AuthorFilterBooksLibrary.get_books(library, author)

    for book in book_list:
        print(book)


if __name__ == "__main__":
    execute_application()
