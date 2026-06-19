from src.product import Product


def test_base_product(capsys):
    _ = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    captured = capsys.readouterr()
    assert "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', '180000.0', '5')" in captured.out
