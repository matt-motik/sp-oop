"""Модуль базового класса для сущностей, содержащих товары и имеющих общую стоимость.."""

from abc import ABC
from abc import abstractmethod


class BaseContainer(ABC):
    """Абстрактный класс для сущностей, содержащих товары и имеющих общую стоимость."""

    @property
    @abstractmethod
    def total_price(self) -> float:  # pragma: no cover
        """Общая стоимость всех товаров в контейнере."""
        pass

    @abstractmethod
    def __str__(self) -> str:  # pragma: no cover
        """Строковое представление контейнера."""
        pass
