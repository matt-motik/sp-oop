"""Модуль для работы с продуктами-Трава газонная."""

from .product import Product


class LawnGrass(Product):
    """Класс, представляющий Траву газонную.

    Attributes:
        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество в наличии.
        country: страна-производитель.
        germination_period: срок прорастания.
        color: цвет.
    """

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует Траву газонную.

        Args:
            name: Название продукта.
            description: Описание продукта.
            price: Цена продукта.
            quantity: Количество в наличии.
            country: страна-производитель.
            germination_period: срок прорастания.
            color: цвет.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: LawnGrass) -> float:  # type: ignore[override]
        """Возвращает полную стоимость всех товаров на складе."""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
