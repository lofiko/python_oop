from typing import TypeVar, Generic, Callable, Optional, Protocol


# ПРОТОКОЛЫ

class Displayable(Protocol):
    def display(self) -> str:
        ...

class Scorable(Protocol):
    def score(self) -> float:
        ...


# TYPEVARS

T = TypeVar('T')
R = TypeVar('R')

D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)


# КОЛЛЕКЦИЯ

class TypedCollection(Generic[T]):

    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        if item in self._items:
            raise ValueError("Такой объект уже есть в коллекции")
        self._items.append(item)

    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Такого объекта нет в коллекции")
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]
    
    def remove_at(self, index: int) -> None:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс за пределами коллекции")
        self._items.pop(index)

    def sort(self, key: Callable[[T], any]) -> None:
        self._items.sort(key=key)

    def find_by_title(self, title: str) -> list[T]:
        return [item for item in self._items if title.lower() in item.title.lower()]

    def find_by_author(self, author: str) -> list[T]:
        return [item for item in self._items if author.lower() in item.author.lower()]

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items] 