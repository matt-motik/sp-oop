from src.order import Order
from src.product import Product


def test_order_init():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    order = Order(product, 3, "Заказ №1", "3 гнусмумса")
    assert order.product == product
    assert order.quantity == 3
    assert order.total_price == product.price * order.quantity
    assert "Заказ №1" == order.name
    assert "3 гнусмумса" == order.description


def test_order_str():
    product = Product("Война и мир", "Толстой Л.Н.", 500, 5)
    order = Order(product, 2, "Заказ №2", " 2шт, война и мир")
    assert str(order) == "Заказ №2: Война и мир x2 = 1000 руб."
