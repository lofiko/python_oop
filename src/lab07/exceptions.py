class ItemNotFoundError(Exception):
    """Объект не найден в коллекции."""
    pass


class DuplicateItemError(Exception):
    """Такой объект уже есть в коллекции."""
    pass


class InvalidInputError(Exception):
    """Некорректный ввод пользователя."""
    pass