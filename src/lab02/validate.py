def validate_title(value):
    if not isinstance(value, str):
        raise TypeError("Название должно быть строкой")
    if not value.strip():
        raise ValueError("Название должно быть непустой строкой")


def validate_author(value):
    if not isinstance(value, str):
        raise TypeError("Автор должен быть строкой")
    if not value.strip():
        raise ValueError("Автор должен быть непустой строкой")


def validate_year(value):
    if not isinstance(value, int):
        raise TypeError("Год издания должен быть целым числом")
    if value < 1450 or value > 2026:
        raise ValueError("Год издания должен быть в диапазоне от 1450 до 2026")


def validate_pages(value):
    if not isinstance(value, int):
        raise TypeError("Количество страниц должно быть целым числом")
    if value <= 0:
        raise ValueError("Количество страниц должно быть больше 0")


def validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Цена должна быть числом")
    if value < 0:
        raise ValueError("Цена не может быть отрицательной")
