"""Модуль для работы с категориями."""

from src.product import Product


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
    products: list[Product]

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
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.products)
