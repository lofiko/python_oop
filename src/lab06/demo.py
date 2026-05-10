from models import PrintedBook, Ebook, AudioBook
from container import TypedCollection

# Создание объектов
book1 = PrintedBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 650, "АСТ", "твёрдый")
book2 = PrintedBook("Преступление и наказание", "Фёдор Достоевский", 1866, 608, 380, "Эксмо", "мягкий")
book3 = Ebook("1984", "Джордж Оруэлл", 1949, 328, 490, "PDF", 2.4)
book4 = Ebook("Дюна", "Фрэнк Херберт", 1965, 688, 820, "EPUB", 4.1)
book5 = AudioBook("Гарри Поттер", "Джоан Роулинг", 2001, 267, 430, 498, "Василий Дахненко")
book6 = AudioBook("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, 290, 132, "Александр Клюквин")

# ============================================================
# Базовая демонстрация TypedCollection
# ============================================================
print("=" * 40)
print("Базовая демонстрация TypedCollection")
print("=" * 40)

collection: TypedCollection = TypedCollection()
collection.add(book1)
collection.add(book2)
collection.add(book3)
collection.add(book4)
collection.add(book5)
collection.add(book6)

print(f"Объектов в коллекции: {len(collection)}")
for book in collection:
    print(f"  - {book.title}")

# Демонстрация защиты от дублей
try:
    collection.add(book1)
except ValueError as e:
    print(f"\nЗащита от дублей: {e}")

# ============================================================
# find, filter, map
# ============================================================
print("\n" + "=" * 40)
print("find, filter, map")
print("=" * 40)

# find — найден
found = collection.find(lambda b: b.price > 700)
print(f"find (цена > 700): {found.title if found else None}")

# find — не найден
not_found = collection.find(lambda b: b.price > 1000)
print(f"find (цена > 1000): {not_found}")

# filter
cheap = collection.filter(lambda b: b.price < 500)
print(f"\nfilter (цена < 500): {len(cheap)} книг")
for book in cheap:
    print(f"  - {book.title}: {book.price:.2f} руб.")

# map — извлечение названий
titles = collection.map(lambda b: b.title)
print(f"\nmap — названия: {titles}")

# map — извлечение цен
prices = collection.map(lambda b: b.price)
print(f"map — цены: {prices}")

# ============================================================
# Сценарий 1 — Protocol Displayable
# ============================================================
print("\n" + "=" * 40)
print("Сценарий 1 — Protocol Displayable")
print("=" * 40)
print("Классы не наследуют Displayable — просто имеют метод display()")

displayable: TypedCollection = TypedCollection()
displayable.add(book1)
displayable.add(book3)
displayable.add(book5)

for item in displayable:
    print(f"  - {item.display()}")

# ============================================================
# Сценарий 2 — Protocol Scorable
# ============================================================
print("\n" + "=" * 40)
print("Сценарий 2 — Protocol Scorable")
print("=" * 40)
print("Классы не наследуют Scorable — просто имеют метод score()")

scorable: TypedCollection = TypedCollection()
scorable.add(book1)
scorable.add(book2)
scorable.add(book3)
scorable.add(book5)

scores = scorable.map(lambda b: (b.title, b.score()))
print("Оценки книг (страниц/руб. или мин./руб.):")
for title, score in scores:
    print(f"  - {title}: {score}")

best = max(scorable.get_all(), key=lambda b: b.score())
print(f"\nЛучшая книга по score: {best.title} ({best.score()})")