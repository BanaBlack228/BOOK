import uuid

from datetime import datetime
from core.enums import GENRES


class Book:

    def __init__(self, title, author, year, genre):
        """
        Конструктор класса Book
        :param title: Название книги
        :param author: Автор книги
        :param year: Год Издания книги
        :param genre: Жанр книги (по умолччанию None)
        :param isbn: ISBN книги (по умолчанию None)

        """
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.__isbn = uuid.uuid4().hex[:9]

    def get_info(self):

        """
        Возвращает строку с информацией о книге
        :return: Строка с информацией о книге

        """

        info = f"{self.title} - {self.author}: {self._year}"
        if self.genre:
            info += f", жанр: {self.genre}"
        info += f", ISBN: {self.__isbn}"
        return info

    @staticmethod
    def is_valid_year(year):
        if isinstance(year, int):
            if 1445 < int(year) < datetime.today().year:
                return True
            else:
                return False
        elif isinstance(year, str):
            if year.isdigit():
                if  1445 < int(year) < datetime.today().year:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def is_older_than(self, year):

        """
        Проверяет была ли книга издана до указанного года.
        :param year: Год Издания книги
        :return: bool

        """
        if self.is_valid_year(year):
            return self._year < year
        else:
            raise ValueError("неверное значение для года издания!")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        if self.is_valid_year(new_year):
            self._year = new_year
        else:
            raise ValueError("Неверное значение для года издания!")

    def get_book_age(self):
        current_year = datetime.today().year
        return current_year - self._year

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        if genre.lower() in GENRES:
            self._genre = genre
        else:
            raise ValueError("Неизвестный жанр!")

    def to_dict(self):
        data = {"author": self.author,
                "title": self.title,
                "year": self.year,
                "genre": self.genre,
                "ISBN": self.__isbn
                }
        return data

# book = Book(title="Капитанская дочка",author="Пушкин", year=1836, genre="роман")

# print(book.get_info())
# book.year = 1837
# print(book.year)
# print(book.get_book_age())
# print(book.is_older_than(year=1700))