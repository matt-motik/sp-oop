"""Модуль для работы с исключениями."""


class QuantityError(Exception):
    """Класс, представляющий исключения при попытке добавить продукт с нулевым количеством."""

    def __init__(self, *args: object) -> None:
        """Инициализирует исключение."""
        self.message: str = str(args[0]) if args else "Товар с нулевым количеством не может быть добавлен"
        super().__init__(self.message)

    def __str__(self) -> str:
        """Строковое представление исключения."""
        return self.message
