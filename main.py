from library_module import *
import json


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

    # Способ 1.
    """
    j = json.dumps(author, default=lambda x: x.__dict__)
    print(j)
    lib = json.dumps(library, default=lambda x: x.__dict__)
    print(lib)
    """

    # Способ 2.
    """
    j = AuthorJSONConverter.to_dict(author)
    d = json.dumps(j)
    print(d)
    """

    # Способ 3. - переопределение метода default
    """
    x = json.dumps(author, cls=TestEncoder)
    print(x)
    """

    # Способ 4.

    x = JSONAuthorAdapter.to_json(author)
    print(x)

    obj = JSONAuthorAdapter.from_json(x)
    print(obj)


if __name__ == "__main__":
    execute_application()
