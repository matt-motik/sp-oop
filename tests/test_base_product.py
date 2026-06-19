from src.product import Product


def test_base_product(capsys):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product1.price == 180000.0
    product2.price = 220000.0
    assert product2.price == 220000.0