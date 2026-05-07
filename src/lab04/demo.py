from models import PrintedBook, Ebook, AudioBook
from collection import Library
from interfaces import Printable, Comparable

#класс без comprable (для проверки)
class SimpleNote(Printable):
    def __init__(self, text):
        self._text = text

    def to_string(self):
        return f"Заметка: {self._text}"
    

# Создание объектов
book1 = PrintedBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 650, "АСТ", "твёрдый")
book2 = PrintedBook("Преступление и наказание", "Фёдор Достоевский", 1866, 608, 380, "Эксмо", "мягкий")
book3 = Ebook("1984", "Джордж Оруэлл", 1949, 328, 490, "PDF", 2.4)
book4 = Ebook("Дюна", "Фрэнк Херберт", 1965, 688, 820, "EPUB", 4.1)
book5 = AudioBook("Гарри Поттер", "Джоан Роулинг", 2001, 267, 430, 498, "Василий Дахненко")
book6 = AudioBook("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, 290, 132, "Александр Клюквин")
note = SimpleNote("Список книг для чтения") # для проверки

library = Library()
library.add(book1)
library.add(book2)
library.add(book3)
library.add(book4)
library.add(book5)
library.add(book6)

# Сценарий 1 — вызов to_string() через интерфейс Printable
print("=" * 40)
print("Сценарий 1 — полиморфизм через to_string()")
print("=" * 40)
for book in library:
    print(book.to_string())

# Сценарий 2 — универсальная функция через интерфейс
print("\n" + "=" * 40)
print("Сценарий 2 — универсальная функция")
print("=" * 40)

def print_all(items: list):
    for item in items:
        if isinstance(item, Printable):
            print(item.to_string())

print_all(library.get_all())

# Сценарий 3 — сравнение через compare_to()
print("\n" + "=" * 40)
print("Сценарий 3 — сравнение объектов")
print("=" * 40)
result = book1.compare_to(book3)
if result < 0:
    print(f"{book1.title} дешевле чем {book3.title} на {abs(result):.2f} руб.")
elif result > 0:
    print(f"{book1.title} дороже чем {book3.title} на {abs(result):.2f} руб.")
else:
    print(f"{book1.title} и {book3.title} стоят одинаково")

# Сценарий 4 — проверка через isinstance()
print("\n" + "=" * 40)
print("Сценарий 4 — проверка интерфейсов")
print("=" * 40)
for obj in [book1, book2, book3, note]:
    is_printable = isinstance(obj, Printable)
    is_comparable = isinstance(obj, Comparable)
    print(f"{obj.to_string()[:30]}: Printable={is_printable}, Comparable={is_comparable}")

# Сценарий 5 — фильтрация по интерфейсу
print("\n" + "=" * 40)
print("Сценарий 5 — фильтрация по интерфейсу")
print("=" * 40)
printable = library.get_printable()
print(f"Объектов реализующих Printable: {len(printable)}")
for book in printable:
    print(f"  - {book.to_string()}")

# Сценарий 6 — сортировка через compare_to()
print("\n" + "=" * 40)
print("Сценарий 6 — сортировка по цене")
print("=" * 40)
library.sort(key=lambda book: book.price)
for book in library:
    print(f"  - {book.title}: {book.price:.2f} руб.")