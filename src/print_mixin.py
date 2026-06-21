"""Модуль для работы с mixin."""

from typing import Protocol
from typing import TypeVar


class ProductProtocol(Protocol):
    """Протокол для миксина."""

    name: str
    description: str
    price: float
    quantity: int


P = TypeVar("P", bound=ProductProtocol)


class PrintMixin:
    """Класс, представляющий Репрезентацию экземпляра."""

    def __init__(self: P) -> None:
        """Инициализирует mixin."""
        print(self.__repr__())

    def __repr__(self: P) -> str:
        """Репрезентация экземпляра."""
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', '{self.price}', '{self.quantity}')"
        # Product('Продукт1', 'Описание продукта', 1200, 10)
