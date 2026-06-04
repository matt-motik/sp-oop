"""Модуль для работы с категориями."""

from typing import TYPE_CHECKING

from .logger_creator import create_logger
from .product import Product

if TYPE_CHECKING:
    from .category_iterator import CategoryIterator  # noqa: F401

logger = create_logger(__name__)


class Category:
    """Класс, представляющий категорию продуктов.

    Attributes:
        name: Название категории.
        description: Описание категории.
        products: Список продуктов в категории.
        category_count: Общее количество категорий (атрибут класса).
        product_count: Общее количество продуктов во всех категориях (атрибут класса).
    """

    name: str
    description: str
    __products: list[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product] | None) -> None:
        """Инициализирует категорию.

        Args:
            name: Название категории.
            description: Описание категории.
            products: Список продуктов в категории.
        """
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Возвращает: Название категории, количество продуктов: X шт."""
        return f"{self.name}, количество продуктов: {sum(p.quantity for p in self.__products)} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список товаров категории.

        Args:
            product: Объект класса Product для добавления.
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            logger.error("product должен быть типа Product")

    @property
    def products(self) -> str:
        r"""Возвращает отформатированную строку со списком товаров категории.

        Returns:
            Строка, содержащая информацию о каждом товаре в формате:
            "Название продукта, X руб. Остаток: X шт.\n"

        Example:
            >>> cat = Category("Телефоны", "Смартфоны", [])
            >>> cat.add_product(Product("iPhone 15", "Apple", 210000.0, 8))
            >>> print(cat.products)
            iPhone 15, 210000.0 руб. Остаток: 8 шт.
        """
        return "".join((f"{p}\n" for p in self.__products))

    @property
    def products_list(self) -> list[Product]:
        r"""Возвращает список товаров категории.

        Returns:
            список товаров

        Example:
            >>> cat = Category("Телефоны", "Смартфоны", [])
            >>> cat.add_product(Product("iPhone 15", "Apple", 210000.0, 8))
            >>> print(cat.products_list[0])
            iPhone 15, 210000.0 руб. Остаток: 8 шт.
        """
        return self.__products

    def __iter__(self) -> CategoryIterator:
        """Делает объект Category итерируемым, возвращая CategoryIterator."""
        from .category_iterator import CategoryIterator  # noqa: F811

        return CategoryIterator(self)
