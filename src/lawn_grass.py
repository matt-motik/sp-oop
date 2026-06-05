"""Модуль для работы с продуктами-Трава газонная."""

from  .product import Product

class LawnGrass(Product):
    """Класс, представляющий Трава газонная.

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


    def __init__(self, name, description, price, quantity, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
