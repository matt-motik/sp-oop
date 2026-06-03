"""Модуль с итератором для категории."""

from .category import Category
from .product import Product


class CategoryIterator:
    """Итератор для безопасного перебора товаров в категории."""

    def __init__(self, category: Category):
        """Инициализирует итератор.

        Args:
            category: Объект категории, товары которого нужно перебрать.

        Raises:
            TypeError: Если передан объект не типа Category.
        """
        if not isinstance(category, Category):
            raise TypeError(f"Ожидался объект Category, получен {type(category).__name__}")
        self.__products = category.products_list
        self.__index = 0

    def __iter__(self) -> CategoryIterator:
        """Возвращает сам объект итератора и сбрасывает индекс."""
        self.__index = 0
        return self

    def __next__(self) -> Product:
        """Возвращает следующий продукт или выбрасывает StopIteration."""
        if self.__index < len(self.__products):
            product = self.__products[self.__index]
            self.__index += 1
            return product
        else:
            raise StopIteration
