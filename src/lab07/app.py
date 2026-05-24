from typing import Optional
from model import Book
from models import PrintedBook, Ebook, AudioBook
from exceptions import ItemNotFoundError, DuplicateItemError
import storage
import os

class LibraryApp:
    """Бизнес-логика библиотечного приложения."""

    FILEPATH = os.path.join(os.path.dirname(__file__), "library.json")

    def __init__(self) -> None:
        """Инициализация приложения и загрузка данных."""
        self._books: list = []
        self.load()

    def load(self) -> None:
        """Загрузить данные из файла."""
        self._books = storage.load(self.FILEPATH)

    def save(self) -> None:
        """Сохранить данные в файл."""
        storage.save(self._books, self.FILEPATH)

    def get_all(self) -> list:
        """Получить все книги."""
        return list(self._books)

    def add(self, book: Book) -> None:
        """Добавить книгу в коллекцию."""
        for existing in self._books:
            if existing == book:
                raise DuplicateItemError(f"Книга '{book.title}' уже есть в библиотеке")
        self._books.append(book)

    def remove(self, title: str) -> None:
        """Удалить книгу по названию."""
        for book in self._books:
            if book.title.lower() == title.lower():
                self._books.remove(book)
                return
        raise ItemNotFoundError(f"Книга '{title}' не найдена")

    def find_by_title(self, title: str) -> list:
        """Найти книги по названию."""
        return [b for b in self._books if title.lower() in b.title.lower()]

    def find_by_author(self, author: str) -> list:
        """Найти книги по автору."""
        return [b for b in self._books if author.lower() in b.author.lower()]

    def filter_by_price(self, min_price: float, max_price: float) -> list:
        """Фильтрация по диапазону цен."""
        return [b for b in self._books if min_price <= b.price <= max_price]

    def filter_available(self) -> list:
        """Фильтрация по доступности."""
        return [b for b in self._books if b.is_available]

    def sort_by_title(self) -> None:
        """Сортировка по названию."""
        self._books.sort(key=lambda b: b.title)

    def sort_by_price(self) -> None:
        """Сортировка по цене."""
        self._books.sort(key=lambda b: b.price)

    def sort_by_year(self) -> None:
        """Сортировка по году."""
        self._books.sort(key=lambda b: b.year)