"""Модуль для работы с продуктами."""
from .print_mixin import PrintMixin
from .base_product import BaseProduct
from .logger_creator import create_logger
from .utils import confirm

logger = create_logger(__name__)


class Product(BaseProduct, PrintMixin):
    """Класс, представляющий продукт.

    Attributes:
        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество в наличии.
    """

    name: str
    description: str
    __price: float
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
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        """Возвращает Название продукта, X руб. Остаток: X шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        """Возвращает полную стоимость всех товаров на складе."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product: dict, products: list[Product] | None = None) -> Product:
        """Создаёт экземпляр Product из словаря или обновляет существующий товар.

        Args:
            product: Словарь с данными продукта (ключи: name, description, price, quantity).
            products: Опциональный список существующих товаров для проверки дубликатов по имени.

        Returns:
            Новый экземпляр Product, либо обновлённый существующий объект при совпадении имени.

        Example:
            >>> data = {"name": "iPhone", "description": "Apple", "price": 1000.0, "quantity": 5}
            >>> Product.new_product(data)
            <Product object at ...>
            >>> existing = [Product("iPhone", "Apple", 900.0, 3)]
            >>> Product.new_product(data, existing)  # Обновит existing: quantity=8, price=1000.0
        """
        if products is None:
            return cls(**product)
        else:
            res = list(filter(lambda x: x.name == product["name"], products))
            if len(res) > 0:
                res[0].__price = max(product["price"], res[0].__price)
                res[0].quantity += product["quantity"]
                return res[0]
            else:
                return cls(**product)

    @property
    def price(self) -> float:
        """Геттер для получения цены продукта.

        Returns:
            Текущее значение цены товара.

        Example:
            >>> p = Product("iPhone 15", "Apple", 210000.0, 8)
            >>> p.price
            210000.0
        """
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер для установки или обновления цены продукта.

        Args:
            price: Новое значение цены. Должно быть строго больше 0.
                   При попытке снижения цены запрашивается ручное подтверждение.

        Example:
            >>> p = Product("iPhone 15", "Apple", 210000.0, 8)
            >>> p.price = 250000.0  # Повышение: обновляется без подтверждения
            >>> p.price
            250000.0
            >>> p.price = -50  # Отрицательное значение: обновление отклонено
            Цена не должна быть нулевая или отрицательная
        """
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            logger.warning("Цена не должна быть нулевая или отрицательная")
            return
        if price <= self.__price:
            if confirm("Вы уверены, что хотите снизить цену? (y/n): "):
                print("Действие выполнено")
                self.__price = price
            else:
                print("Действие отменено")
        else:
            self.__price = price
