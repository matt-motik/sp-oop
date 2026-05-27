"""Модуль для работы с категориями."""
from .logger_creator import create_logger


from src.product import Product

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

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        logger.error("product должен быть типа Product")

    @property
    def products(self) -> str:
        return "\n".join((f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products))