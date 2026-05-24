from app import LibraryApp
from models import PrintedBook, Ebook, AudioBook
from exceptions import ItemNotFoundError, DuplicateItemError, InvalidInputError


class CLI:
    """Консольный интерфейс библиотечного приложения."""

    def __init__(self, app: LibraryApp) -> None:
        """Инициализация CLI с экземпляром приложения."""
        self._app = app

    def run(self) -> None:
        """Запустить главный цикл приложения."""
        print("Добро пожаловать в библиотеку!")
        if self._app.get_all():
            print(f"Загружено книг: {len(self._app.get_all())}")

        while True:
            self._show_menu()
            try:
                choice = int(input("\nВыберите пункт: "))
            except ValueError:
                print("Ошибка: введите число")
                continue

            if choice == 0:
                self._app.save()
                print("Данные сохранены. До свидания!")
                break
            elif choice == 1:
                self._show_all()
            elif choice == 2:
                self._add_book()
            elif choice == 3:
                self._find_book()
            elif choice == 4:
                self._filter_books()
            elif choice == 5:
                self._sort_books()
            elif choice == 6:
                self._remove_book()
            else:
                print("Ошибка: такого пункта нет")

    def _show_menu(self) -> None:
        """Показать главное меню."""
        print("\n" + "=" * 40)
        print("         БИБЛИОТЕКА")
        print("=" * 40)
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Найти книгу")
        print("4. Фильтрация")
        print("5. Сортировка")
        print("6. Удалить книгу")
        print("0. Выход")
        print("=" * 40)

    def _show_books(self, books: list) -> None:
        """Вывести список книг."""
        if not books:
            print("Книг не найдено.")
            return
        print(f"\nНайдено книг: {len(books)}")
        print("-" * 40)
        for i, book in enumerate(books, 1):
            book_type = type(book).__name__
            status = "доступна" if book.is_available else "выдана"
            print(f"{i}. [{book_type}] {book.title}")
            print(f"   Автор: {book.author}, {book.year} г.")
            print(f"   Цена: {book.price:.2f} руб. | Статус: {status}")
            if isinstance(book, PrintedBook):
                print(f"   Издательство: {book.publisher}, переплёт: {book.cover_type}")
            elif isinstance(book, Ebook):
                print(f"   Формат: {book.file_format}, размер: {book.file_size} МБ")
            elif isinstance(book, AudioBook):
                print(f"   Длительность: {book.duration} мин., чтец: {book.narrator}")
            print("-" * 40)

    def _show_all(self) -> None:
        """Показать все книги."""
        books = self._app.get_all()
        self._show_books(books)

    def _add_book(self) -> None:
        """Добавить новую книгу."""
        print("\nТип книги:")
        print("1. Бумажная книга")
        print("2. Электронная книга")
        print("3. Аудиокнига")

        try:
            book_type = int(input("Выберите тип: "))
            if book_type not in [1, 2, 3]:
                raise InvalidInputError("Неверный тип книги")

            title = input("Название: ").strip()
            author = input("Автор: ").strip()
            year = int(input("Год издания: "))
            pages = int(input("Количество страниц: "))
            price = float(input("Цена: "))

            if book_type == 1:
                publisher = input("Издательство: ").strip()
                cover_type = input("Тип переплёта: ").strip()
                book = PrintedBook(title, author, year, pages, price, publisher, cover_type)
            elif book_type == 2:
                file_format = input("Формат файла (PDF/EPUB): ").strip()
                file_size = float(input("Размер файла (МБ): "))
                book = Ebook(title, author, year, pages, price, file_format, file_size)
            else:
                duration = int(input("Длительность (мин.): "))
                narrator = input("Чтец: ").strip()
                book = AudioBook(title, author, year, pages, price, duration, narrator)

            self._app.add(book)
            print(f"Книга '{title}' успешно добавлена!")

        except DuplicateItemError as e:
            print(f"Ошибка: {e}")
        except InvalidInputError as e:
            print(f"Ошибка: {e}")
        except (ValueError, TypeError) as e:
            print(f"Ошибка ввода: {e}")

    def _find_book(self) -> None:
        """Найти книгу."""
        print("\nПоиск по:")
        print("1. Названию")
        print("2. Автору")

        try:
            choice = int(input("Выберите: "))
            if choice == 1:
                title = input("Введите название: ").strip()
                books = self._app.find_by_title(title)
            elif choice == 2:
                author = input("Введите автора: ").strip()
                books = self._app.find_by_author(author)
            else:
                raise InvalidInputError("Неверный пункт")

            self._show_books(books)

        except InvalidInputError as e:
            print(f"Ошибка: {e}")
        except ValueError:
            print("Ошибка: введите число")

    def _filter_books(self) -> None:
        """Фильтрация книг."""
        print("\nФильтрация по:")
        print("1. Диапазону цен")
        print("2. Доступности")

        try:
            choice = int(input("Выберите: "))
            if choice == 1:
                min_price = float(input("Минимальная цена: "))
                max_price = float(input("Максимальная цена: "))
                books = self._app.filter_by_price(min_price, max_price)
            elif choice == 2:
                books = self._app.filter_available()
            else:
                raise InvalidInputError("Неверный пункт")

            self._show_books(books)

        except InvalidInputError as e:
            print(f"Ошибка: {e}")
        except ValueError:
            print("Ошибка: введите число")

    def _sort_books(self) -> None:
        """Сортировка книг."""
        print("\nСортировать по:")
        print("1. Названию")
        print("2. Цене")
        print("3. Году")

        try:
            choice = int(input("Выберите: "))
            if choice == 1:
                self._app.sort_by_title()
                print("Отсортировано по названию.")
            elif choice == 2:
                self._app.sort_by_price()
                print("Отсортировано по цене.")
            elif choice == 3:
                self._app.sort_by_year()
                print("Отсортировано по году.")
            else:
                raise InvalidInputError("Неверный пункт")

            self._show_all()

        except InvalidInputError as e:
            print(f"Ошибка: {e}")
        except ValueError:
            print("Ошибка: введите число")

    def _remove_book(self) -> None:
        """Удалить книгу с подтверждением."""
        title = input("\nВведите название книги для удаления: ").strip()
        confirm = input(f"Удалить '{title}'? (y/n): ").strip().lower()

        if confirm != 'y':
            print("Удаление отменено.")
            return

        try:
            self._app.remove(title)
            print(f"Книга '{title}' удалена.")
        except ItemNotFoundError as e:
            print(f"Ошибка: {e}")