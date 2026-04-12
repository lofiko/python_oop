from base import Book

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