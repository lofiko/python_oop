from abc import ABC
from interfaces import Printable, Comparable

from validate import validate_title, validate_author, validate_year, validate_pages, validate_price
from interfaces import Printable, Comparable

from validate import (
    validate_title,
    validate_author,
    validate_year,
    validate_pages,
    validate_price
)


class Book(Printable, Comparable):
    total_books = 0

    def __init__(self, title: str, author: str, year: int, pages: int, price: float):

        validate_title(title)
        validate_author(author)
        validate_year(year)
        validate_pages(pages)
        validate_price(price)

        self._title = title.strip()
        self._author = author.strip()
        self._year = year
        self._pages = pages
        self._price = float(price)
        self._is_available = True

        Book.total_books += 1


    # СВОЙСТВА

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def pages(self):
        return self._pages

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        validate_price(value)
        self._price = float(value)

    @property
    def is_available(self):
        return self._is_available


    # СОСТОЯНИЕ

    def borrow(self):
        if not self._is_available:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def return_book(self):
        if self._is_available:
            raise ValueError("Книга уже находится в библиотеке")
        self._is_available = True


    # БИЗНЕС-МЕТОДЫ

    def discount(self, percent: float):
        if not isinstance(percent, (int, float)):
            raise TypeError("Скидка должна быть числом")
        if percent < 0 or percent > 100:
            raise ValueError("Скидка должна быть от 0 до 100")

        self._price *= (1 - percent / 100)

    def is_classic(self):
        return self._year < 1970


    # МАГИЧЕСКИЕ МЕТОДЫ

    def __str__(self):
        status = "Доступна" if self._is_available else "Выдана"
        return (
            f"Книга: {self._title}\n"
            f"Автор: {self._author}\n"
            f"Год: {self._year}\n"
            f"Страниц: {self._pages}\n"
            f"Цена: {self._price:.2f} руб.\n"
            f"Статус: {status}"
        )

    def __repr__(self):
        return (
            f"Book(title='{self._title}', author='{self._author}', "
            f"year={self._year}, pages={self._pages}, price={self._price}, "
            f"is_available={self._is_available})"
        )

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self._title == other._title
            and self._author == other._author
            and self._year == other._year
        )


    # ИНТЕРФЕЙСЫ

    def to_string(self):
        return f"{self._title} - {self._author}, {self._year}, {self._price:.2f} руб."
    
    def compare_to(self, other):
        if not isinstance(other, Book):
            raise TypeError("Можно сравнивать только с классом Book")
        return self._price - other._price
    

class PrintedBook(Book):
    def __init__(self, title, author, year, pages, price, publisher, cover_type):
        super().__init__(title, author, year, pages, price)
        self._publisher = publisher
        self._cover_type = cover_type

    @property
    def publisher(self):
        return self._publisher
    
    @property
    def cover_type(self):
        return self._cover_type
    
    def get_info(self):
        return f"{self._title} - {self._author}, {self._year} | Издательство: {self._publisher}, переплет: {self._cover_type}"
    
    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Издательство: {self._publisher}\n"
            f"Переплет: {self._cover_type}" 
        )
    
    def to_string(self):
        return f"{self._title} — {self._author}, {self._year} | Издательство: {self._publisher}, переплёт: {self._cover_type}, {self._price:.2f} руб."

    def compare_to(self, other):
        if not isinstance(other, Book):
            raise TypeError("Можно сравнивать только с Book")
        return self._price - other._price
    
class Ebook(Book):
    def __init__(self, title, author, year, pages, price, file_format, file_size):
        super().__init__(title, author, year, pages, price)
        self._file_format = file_format
        self._file_size = file_size

    @property
    def file_format(self):
        return self._file_format
    
    @property
    def file_size(self):
        return self._file_size
    
    def get_info(self):
        return f"{self._title} - {self._author}, {self._year} | Формат: {self._file_format}, размер: {self._file_size} МБ"
    
    def __str__(self):
        return(
            f"{super().__str__()}\n"
            f"Формат: {self._file_format}\n"
            f"Размер файла: {self._file_size} МБ"
        )
    
    def to_string(self):
        return f"{self._title} — {self._author}, {self._year} | Формат: {self._file_format}, размер: {self._file_size} МБ, {self._price:.2f} руб."

    def compare_to(self, other):
        if not isinstance(other, Book):
            raise TypeError("Можно сравнивать только с Book")
        return self._price - other._price

class AudioBook(Book):
    def __init__(self, title, author, year, pages, price, duration, narrator):
        super().__init__(title, author, year, pages, price)
        self._duration = duration #длительность
        self._narrator = narrator #чтец

    @property
    def duration(self):
        return self._duration

    @property
    def narrator(self):
        return self._narrator

    def get_info(self):
        return f"{self._title} — {self._author}, {self._year} | Длительность: {self._duration} мин., чтец: {self._narrator}"

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Длительность: {self._duration} мин.\n"
            f"Чтец: {self._narrator}"
        )
    
    def to_string(self):
        return f"{self._title} — {self._author}, {self._year} | Длительность: {self._duration} мин., чтец: {self._narrator}, {self._price:.2f} руб."

    def compare_to(self, other):
        if not isinstance(other, Book):
            raise TypeError("Можно сравнивать только с Book")
        return self._price - other._price