"""Модуль для работы с продуктами-смартфонами."""

from  .product import Product

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


    def __init__(self, name, description, price, quantity, efficiency:float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
