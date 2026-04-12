from models import PrintedBook, Ebook, AudioBook
from collection import Library

# cоздание объектов
book1 = PrintedBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 650, "АСТ", "твёрдый")
book2 = PrintedBook("Преступление и наказание", "Фёдор Достоевский", 1866, 608, 380, "Эксмо", "мягкий")
book3 = Ebook("1984", "Джордж Оруэлл", 1949, 328, 490, "PDF", 2.4)
book4 = Ebook("Дюна", "Фрэнк Херберт", 1965, 688, 820, "EPUB", 4.1)
book5 = AudioBook("Гарри Поттер", "Джоан Роулинг", 2001, 267, 430, 498, "Василий Дахненко")
book6 = AudioBook("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, 290, 132, "Александр Клюквин")

library = Library()

# Сценарий 1 — добавление объектов разных типов
print("=" * 40)
print("Сценарий 1 — добавление объектов")
print("=" * 40)
library.add(book1)
library.add(book2)
library.add(book3)
library.add(book4)
library.add(book5)
library.add(book6)
print(f"Книг в библиотеке: {len(library)}")
for book in library:
    print(f"  - {book.get_info()}")

# Сценарий 2 — проверка типов
print("\n" + "=" * 40)
print("Сценарий 2 — проверка типов")
print("=" * 40)
for book in library:
    if isinstance(book, PrintedBook):
        print(f"{book.title} — бумажная книга, издательство: {book.publisher}")
    elif isinstance(book, Ebook):
        print(f"{book.title} — электронная книга, формат: {book.file_format}")
    elif isinstance(book, AudioBook):
        print(f"{book.title} — аудиокнига, чтец: {book.narrator}")

# Сценарий 3 — полиморфизм через get_info()
print("\n" + "=" * 40)
print("Сценарий 3 — полиморфизм")
print("=" * 40)
for book in library:
    print(book.get_info())

# Сценарий 4 — фильтрация по типу
print("\n" + "=" * 40)
print("Сценарий 4 — фильтрация по типу")
print("=" * 40)

printed = library.get_only_printed()
print(f"Бумажные книги: {len(printed)}")
for book in printed:
    print(f"  - {book.title} ({book.publisher})")

ebooks = library.get_only_ebooks()
print(f"\nЭлектронные книги: {len(ebooks)}")
for book in ebooks:
    print(f"  - {book.title} ({book.file_format})")

audiobooks = library.get_only_audiobooks()
print(f"\nАудиокниги: {len(audiobooks)}")
for book in audiobooks:
    print(f"  - {book.title} ({book.narrator})")

# Сценарий 5 — полный вывод через __str__
print("\n" + "=" * 40)
print("Сценарий 5 — полный вывод объектов")
print("=" * 40)
print(book1)
print()
print(book3)
print()
print(book5)