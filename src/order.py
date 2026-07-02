"""Модуль для работы с заказами."""

from exceptions import QuantityError

from .base_container import BaseContainer
from .logger_creator import create_logger
from .product import Product

logger = create_logger(__name__)


class Order(BaseContainer):
    """Класс, представляющий заказ на один товар."""

    def __init__(self, product: Product, quantity: int, name: str, description: str):
        """
        Инициализирует заказ.

        Args:
            product: Товар, который заказывают.
            quantity: Количество товара.
            name: Название заказа.
            description: Описание заказа.
        """
        try:
            if not isinstance(product, Product):
                logger.error("В заказ можно добавлять только объекты типа Product или его наследников")
                raise TypeError("В заказ можно добавлять только объекты типа Product или его наследников")
            if product.quantity <= 0:
                raise QuantityError
        except TypeError as e:
            logger.error(e)
            print(e)
        except QuantityError as e:
            logger.error(e)
            print(e)
        else:
            self.product = product
            print("Товар успешно добавлен")
        finally:
            print("Добавление завершено")
        self.quantity = quantity
        self.name = name
        self.description = description

    @property
    def total_price(self) -> float:
        """Итоговая стоимость заказа."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        """Возвращает строковое представление заказа."""
        return f"{self.name}: {self.product.name} x{self.quantity} = {self.total_price} руб."
