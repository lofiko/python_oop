from model import Book

# Сценарий 1 — создание объекта
book1 = Book("Истребление тиранов", "Владимир Набоков", 1938, 128, 650)
print("Сценарий 1 — создание объекта:")
print(book1)

# Сценарий 2 — сравнение объектов
book2 = Book("Истребление тиранов", "Владимир Набоков", 1938, 140, 700)
print("\nСценарий 2 — сравнение объектов:")
print("Книги равны?", book1 == book2)

# Сценарий 3 — изменение через setter
book1.price = 590
print("\nСценарий 3 — изменение через setter:")
print("Новая цена:", f"{book1.price:.2f} руб.")

# Сценарий 4 — второй бизнес-метод
print("\nСценарий 4 — проверка бизнес-метода:")
print("Книга является классикой?", book1.is_classic())

# Сценарий 5 — скидка
book1.discount(10)
print("\nСценарий 5 — применение скидки:")
print("Цена после скидки 10%:", f"{book1.price:.2f} руб.")

# Сценарий 6 — логическое состояние
book1.borrow()
print("\nСценарий 6 — после выдачи книги:")
print(book1)

try:
    book1.borrow()
except ValueError as e:
    print("\nОшибка при повторной выдаче:", e)

book1.return_book()
print("\nПосле возврата книги:")
print(book1)

try:
    book1.return_book()
except ValueError as e:
    print("\nОшибка при повторном возврате:", e)

# Сценарий 7 — демонстрация валидации
try:
    bad_book = Book("", "Автор", -10, 0, -100)
except (TypeError, ValueError) as e:
    print("\nОшибка создания объекта:", e)

# Сценарий 8 — атрибут класса
print("\nСценарий 8 — атрибут класса:")
print("Всего создано книг:", Book.total_books)
print("Доступ через экземпляр:", book1.total_books)

# Сценарий 9 — repr
print("\nСценарий 9 — __repr__:")
print(repr(book1))
