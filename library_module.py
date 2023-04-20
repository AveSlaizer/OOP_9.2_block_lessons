import copy
from abc import abstractmethod

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

    @year.setter
    def year(self, year: int):
        self.__year = year

    def __str__(self):
        return f"{self.__name} {self.__surname} {self.__year}"

    def __eq__(self, other):
        if isinstance(other, Author):
            return self.__name == other.__name and self.__surname == other.__surname and self.__year == other.__year
        raise TypeError(f"Невозможно сравнить с объектом {other.__class__.__name__}")

    def __hash__(self):
        return hash((self.__name, self.__surname, self.__year))


class Book:

    def __init__(self, title: str, genre: str, author: Author):
        self.__title = title
        self.__author = author
        self.__genre = genre
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

    def __str__(self):
        return f"< Название: {self.title}, автор: {self.author} >"


class Reader:

    def __init__(self, name: str, ticket: int):
        self.__name = name
        self.__ticket = ticket
        self.__books = []

    @property
    def name(self):
        return self.__name

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


class SearchingObjects:

    @abstractmethod
    def get_objects(self):
        raise NotImplementedError


class Library(SearchingObjects):

    def __init__(self, name: str):
        self.__name = name
        self.__books = []
        self.__readers = []

    @property
    def books(self):
        return self.__books

    def add_book(self, book: Book):
        self.__books.append(copy.deepcopy(book))

    def del_book(self, title: str):
        for index, book in enumerate(self.__books):
            if book.title == title:
                return self.__books.pop(index)
        raise FoundBookError(f"В библиотеке отсутствует книга с названием {title}")

    def print_books(self):
        for index, book in enumerate(self.__books, start=1):
            print(f"{index}) {book}")

    def get_objects(self):
        for book in self.__books:
            yield book


class FilterLibrary:

    @staticmethod
    @abstractmethod
    def get_books(library: Library, key):
        raise NotImplementedError


class GenreFilterBooksLibrary(FilterLibrary):

    @staticmethod
    def get_books(library: Library, genre: str):
        books = library.get_objects()
        for book in books:
            if book.genre == genre:
                yield book


class AuthorFilterBooksLibrary(FilterLibrary):

    @staticmethod
    def get_books(library: Library, author: Author):
        books = library.get_objects()
        for book in books:
            if book.author == author:
                yield book
