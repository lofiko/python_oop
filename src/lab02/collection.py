from model import Book


class Library:
    def __init__(self):
        self._items = []

# на 3
    def add(self, item):
        if not isinstance(item, Book):
            raise TypeError("Можно добавлять только объекты Book")
        if item in self._items:
            raise ValueError("Такая Книга уже есть в библиотеке")
        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            raise ValueError("Такой книги нет в библиотеке")
        self._items.remove(item)

    def get_all(self):
        return list(self._items)
    
# на 4    
    def find_by_title(self, title):
        return [item for item in self._items if title.lower() in item.title.lower()]
    
    def find_by_author(self, author):
        return [item for item in self._items if author.lower() in item.author.lower()]
    
    # магические 
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
# на 5
    def __getitem__(self, index):
        return self._items[index]
    
    def remove_at(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс за пределами коллекции")
        self._items.pop(index)

    def sort(self, key):
        self._items.sort(key=key)

    # лог операции
    def get_available(self):
        result = Library()
        for item in self._items:
            if item.is_available:
                result.add(item)
        return result
    
    def get_classic(self):
        result = Library()
        for item in self._items:
            if item.is_classic():
                result.add(item)
        return result
    
    def get_long_reads(self, threshold=300):
        result = Library()
        for item in self._items:
            if item.pages > threshold:
                result.add(item)
        return result