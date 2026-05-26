"""Модуль для работы с продуктами."""


class Product:
    """Класс, представляющий продукт.

    Attributes:
        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество в наличии.
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует продукт.

        Args:
            name: Название продукта.
            description: Описание продукта.
            price: Цена продукта.
            quantity: Количество в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
