from model import Book

class Library:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Book):
            raise TypeError("Можно добавлять только объекты Book")
        if item in self._items:
            raise ValueError("Такая книга уже есть в библиотеке")
        self._items.append(item)
        
    def get_all(self):
        return list(self._items)
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
            return self._items[index]
    
    def sort_by(self, key_func):
        self._items.sort(key=key_func)
        return self
    
    def filter_by(self, predicate):
        result = Library()
        for item in self._items:
            if predicate(item):
                result.add(item)
        return result
    
    def apply(self, func):
        for item in self._items:
            func(item)
        return self
    

