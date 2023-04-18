import copy

"""
Реализовать классы Книга, Автор, Читатель, доп: Библиотека
Описать требуемые зависимости
Протестировать функциональность:
    - Создать книгу
    - Создать читателя
    - Выдать читателю книгу
    - Поменять читателю книгу

"""


class FoundBookError(Exception):

    def __init__(self, text: str):
        self.text = text


class Author:

    def __init__(self, name: str, surname: str, year: int):
        self.__name = name
        self.__surname = surname
        self.__year = year

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def year(self):
        return self.__year


class Book:

    def __init__(self, title: str, author: Author):
        self.__title = title
        self.__author = author
        self.__genre = None
        self.__page_qty = 0

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

    @property
    def page_qty(self):
        return self.__page_qty

    @page_qty.setter
    def page_qty(self, page_qty: int):
        self.__page_qty = page_qty


class Reader:

    def __init__(self, name: str, ticket: int):
        self.__name = name
        self.__ticket = ticket
        self.__books = []

    @property
    def books(self):
        return self.__books

    def take_book(self, book: Book):
        self.__books.append(book)

    def give_book(self, title: str):
        for index, book in enumerate(self.__books):
            if book.title == title:
                return self.__books.pop(index)
        raise FoundBookError(f"У читателя отсутствует книга {title}")


class Library:
    pass
