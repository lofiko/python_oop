from models import PrintedBook, Ebook, AudioBook
from collection import Library
from strategies import (
    by_title, by_price, by_year,
    is_available, is_classic, is_printed,
    make_price_filter, make_year_filter,
    DiscountStrategy, PriceIncreaseStrategy
)

# Создание объектов
book1 = PrintedBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 650, "АСТ", "твёрдый")
book2 = PrintedBook("Преступление и наказание", "Фёдор Достоевский", 1866, 608, 380, "Эксмо", "мягкий")
book3 = Ebook("1984", "Джордж Оруэлл", 1949, 328, 490, "PDF", 2.4)
book4 = Ebook("Дюна", "Фрэнк Херберт", 1965, 688, 820, "EPUB", 4.1)
book5 = AudioBook("Гарри Поттер", "Джоан Роулинг", 2001, 267, 430, 498, "Василий Дахненко")
book6 = AudioBook("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, 290, 132, "Александр Клюквин")

library = Library()
library.add(book1)
library.add(book2)
library.add(book3)
library.add(book4)
library.add(book5)
library.add(book6)

# ============================================================
# Сценарий 1 — цепочка filter -> sort -> apply
# ============================================================
print("=" * 40)
print("Сценарий 1 — цепочка операций")
print("=" * 40)

discount = DiscountStrategy(10)

result = library.filter_by(is_available).sort_by(by_price)

print("После фильтрации и сортировки по цене:")
for book in result:
    print(f"  - {book.title}: {book.price:.2f} руб.")

result.apply(discount)

print("\nПосле применения скидки 10%:")
for book in result:
    print(f"  - {book.title}: {book.price:.2f} руб.")

# ============================================================
# Сценарий 2 — замена стратегии без изменения кода коллекции
# ============================================================
print("\n" + "=" * 40)
print("Сценарий 2 — замена стратегии")
print("=" * 40)

library2 = Library()
library2.add(PrintedBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 650, "АСТ", "твёрдый"))
library2.add(Ebook("1984", "Джордж Оруэлл", 1949, 328, 490, "PDF", 2.4))
library2.add(AudioBook("Гарри Поттер", "Джоан Роулинг", 2001, 267, 430, 498, "Василий Дахненко"))

print("Сортировка по названию:")
library2.sort_by(by_title)
for book in library2:
    print(f"  - {book.title}")

print("\nСортировка по году:")
library2.sort_by(by_year)
for book in library2:
    print(f"  - {book.title} ({book.year})")

print("\nСортировка по цене:")
library2.sort_by(by_price)
for book in library2:
    print(f"  - {book.title}: {book.price:.2f} руб.")

# ============================================================
# Сценарий 3 — callable-объект, map, filter, фабрика
# ============================================================
print("\n" + "=" * 40)
print("Сценарий 3 — callable, map, filter, фабрика")
print("=" * 40)

library3 = Library()
library3.add(PrintedBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 650, "АСТ", "твёрдый"))
library3.add(Ebook("1984", "Джордж Оруэлл", 1949, 328, 490, "PDF", 2.4))
library3.add(AudioBook("Гарри Поттер", "Джоан Роулинг", 2001, 267, 430, 498, "Василий Дахненко"))
library3.add(AudioBook("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, 290, 132, "Александр Клюквин"))

# callable-объект
print("Callable-объект — увеличение цены на 20%:")
increase = PriceIncreaseStrategy(20)
library3.apply(increase)
for book in library3:
    print(f"  - {book.title}: {book.price:.2f} руб.")

# map
print("\nmap — извлечение названий:")
titles = list(map(lambda book: book.title, library3))
for title in titles:
    print(f"  - {title}")

# filter + фабрика
print("\nfilter + фабрика — книги дешевле 600 руб.:")
cheap_filter = make_price_filter(600)
cheap = list(filter(cheap_filter, library3))
for book in cheap:
    print(f"  - {book.title}: {book.price:.2f} руб.")

# фабрика по году
print("\nФабрика — книги после 1950 года:")
modern_filter = make_year_filter(1950)
modern = list(filter(modern_filter, library3))
for book in modern:
    print(f"  - {book.title} ({book.year})")