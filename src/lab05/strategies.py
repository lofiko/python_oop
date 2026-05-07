from models import PrintedBook, Ebook, AudioBook

def by_title(book):
    """Сортировка по названию"""
    return book.title

def by_price(book):
    """Сортировка по цене"""
    return book.price

def by_year(book):
    """Сортировка по году издания"""
    return book.year

def is_available(book):
    """Фильтр - только доступные книги"""
    return book.is_available

def is_classic(book):
    """Фильтр - только классика (до 70го)"""
    return book.is_classic()

def is_printed(book):
    """Фильтр - только бумажные книги"""
    return isinstance(book, PrintedBook)

def make_price_filter(max_price):
    """Фабрика - создаёт фильтр по максимальной цене"""
    def filter_fn(book):
        return book.price <= max_price
    return filter_fn

def make_year_filter(min_year):
    """Фабрика - создаёт фильтр по минимальному году"""
    def filter_fn(book):
        return book.year >= min_year
    return filter_fn

class DiscountStrategy:
    """Стратегия - применяет скидку к цене книги"""
    def __init__(self, percent):
        self._percent = percent

    def __call__(self, book):
        book.discount(self._percent)


class PriceIncreaseStrategy:
    """Стратегия - увеличивает цену книги на процент"""
    def __init__(self, percent):
        self._percent = percent

    def __call__(self, book):
        book.price = book.price * (1 + self._percent / 100)