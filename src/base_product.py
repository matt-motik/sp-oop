"""Модуль базового класса продукта."""

from abc import ABC
from abc import abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс продукта."""

    @abstractmethod
    def __add__(self, other: Any) -> float:  # pragma: no cover
        """Возвращает полную стоимость всех товаров на складе."""
        pass

    @abstractmethod
    def __str__(self) -> str:  # pragma: no cover
        """Возвращает строковое представление объекта."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:  # pragma: no cover
        """Геттер для получения цены продукта."""
        pass

    @price.setter
    @abstractmethod
    def price(self, price: float) -> None:  # pragma: no cover
        """Сеттер для установки или обновления цены продукта."""
        pass
