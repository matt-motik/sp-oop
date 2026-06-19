"""Модуль для работы с продуктами-смартфонами."""

from .product import Product


class Smartphone(Product):
    """Класс, представляющий Смартфоны.

    Attributes:
        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество в наличии.
        efficiency: производительность.
        model: модель.
        memory: объем встроенной памяти.
        color: цвет.
    """

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует Смартфон.

        Args:
            name: Название продукта.
            description: Описание продукта.
            price: Цена продукта.
            quantity: Количество в наличии.
            efficiency: производительность.
            model: модель.
            memory: объем встроенной памяти.
            color: цвет.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Smartphone) -> float:  # type: ignore[override]
        """Возвращает полную стоимость всех товаров на складе."""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError
