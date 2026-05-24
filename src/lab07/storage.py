import json
from models import PrintedBook, Ebook, AudioBook


def save(books: list, filepath: str) -> None:
    """Сохранить коллекцию в JSON-файл."""
    data = []
    for book in books:
        item = {
            "type": type(book).__name__,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "pages": book.pages,
            "price": book.price,
            "is_available": book.is_available
        }
        if isinstance(book, PrintedBook):
            item["publisher"] = book.publisher
            item["cover_type"] = book.cover_type
        elif isinstance(book, Ebook):
            item["file_format"] = book.file_format
            item["file_size"] = book.file_size
        elif isinstance(book, AudioBook):
            item["duration"] = book.duration
            item["narrator"] = book.narrator
        data.append(item)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load(filepath: str) -> list:
    """Загрузить объекты из JSON-файла."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    books = []
    for item in data:
        book_type = item["type"]
        if book_type == "PrintedBook":
            book = PrintedBook(
                item["title"], item["author"], item["year"],
                item["pages"], item["price"],
                item["publisher"], item["cover_type"]
            )
        elif book_type == "Ebook":
            book = Ebook(
                item["title"], item["author"], item["year"],
                item["pages"], item["price"],
                item["file_format"], item["file_size"]
            )
        elif book_type == "AudioBook":
            book = AudioBook(
                item["title"], item["author"], item["year"],
                item["pages"], item["price"],
                item["duration"], item["narrator"]
            )
        else:
            continue

        if not item.get("is_available", True):
            book.borrow()

        books.append(book)

    return books