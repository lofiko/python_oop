from model import Book
from collection import Library

# создание объектов
book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 650)
book2 = Book("1984", "Джордж Оруэлл", 1949, 328, 490)
book3 = Book("Дюна", "Фрэнк Херберт", 1965, 688, 820)
book4 = Book("Гарри Поттер", "Джоан Роулинг", 2001, 267, 430)
book5 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 608, 380)

library = Library()

# Сценарий 1 — добавление книг
print("=" * 40)
print("Сценарий 1 — добавление книг")
print("=" * 40)
library.add(book1)
library.add(book2)
library.add(book3)
library.add(book4)
library.add(book5)
print(f"Книг в библиотеке: {len(library)}")
for book in library:
    print(f"  - {book.title} ({book.author})")


# Сценарий 2 — защита от дублей и неверного типа
print("\n" + "=" * 40)
print("Сценарий 2 — защита коллекции")
print("=" * 40)
try:
    library.add(book1)
except ValueError as e:
    print(f"Дубликат: {e}")

try:
    library.add("не книга")
except TypeError as e:
    print(f"Неверный тип: {e}")


# Сценарий 3 — поиск
print("\n" + "=" * 40)
print("Сценарий 3 — поиск")
print("=" * 40)
found = library.find_by_author("оруэлл")
print(f"Поиск по автору 'оруэлл': {len(found)} книг")
for book in found:
    print(f"  - {book.title}")

found = library.find_by_title("д")
print(f"\nПоиск по названию 'д': {len(found)} книг")
for book in found:
    print(f"  - {book.title}")


# Сценарий 4 — индексация и удаление
print("\n" + "=" * 40)
print("Сценарий 4 — индексация и удаление")
print("=" * 40)
print(f"Книга под индексом 0: {library[0].title}")
print(f"Книга под индексом 2: {library[2].title}")

library.remove_at(0)
print(f"\nПосле удаления индекса 0, книг: {len(library)}")
for book in library:
    print(f"  - {book.title}")


# Сценарий 5 — сортировка
print("\n" + "=" * 40)
print("Сценарий 5 — сортировка")
print("=" * 40)
library.sort(key=lambda book: book.title)
print("По названию:")
for book in library:
    print(f"  - {book.title}")

library.sort(key=lambda book: book.price)
print("\nПо цене:")
for book in library:
    print(f"  - {book.title} ({book.price:.2f} руб.)")

library.sort(key=lambda book: book.year)
print("\nПо году:")
for book in library:
    print(f"  - {book.title} ({book.year})")


# Сценарий 6 — фильтрация
print("\n" + "=" * 40)
print("Сценарий 6 — фильтрация")
print("=" * 40)

classics = library.get_classic()
print(f"Классика (до 1970): {len(classics)} книг")
for book in classics:
    print(f"  - {book.title} ({book.year})")

long_reads = library.get_long_reads(400)
print(f"\nДолгое чтение (более 400 стр.): {len(long_reads)} книг")
for book in long_reads:
    print(f"  - {book.title} ({book.pages} стр.)")

book2.borrow()
available = library.get_available()
print(f"\nДоступные книги: {len(available)} из {len(library)}")
for book in available:
    print(f"  - {book.title}")