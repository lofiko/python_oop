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

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]