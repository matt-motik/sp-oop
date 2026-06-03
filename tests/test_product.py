from unittest.mock import patch

import pytest

from src.product import Product


def test_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_new_product():
    data = {"name": "iPhone", "description": "Apple", "price": 1000.0, "quantity": 5}
    product_1 = Product.new_product(data)
    assert product_1.name == "iPhone"
    assert product_1.description == "Apple"
    assert product_1.price == 1000.0
    assert product_1.quantity == 5


def test_new_product_no_in_exist(product_1, product_2, product_3):
    data = {"name": "iPhone", "description": "Apple", "price": 100000.0, "quantity": 5}
    product = Product.new_product(data, [product_1, product_2, product_3])
    assert product.name == "iPhone"
    assert product.description == "Apple"
    assert product.price == 100000.0
    assert product.quantity == 5


def test_new_product_3_in_exist(product_1, product_2, product_3):
    data = {"name": "Iphone 15", "description": "Apple", "price": 1000.0, "quantity": 5}
    product = Product.new_product(data, [product_1, product_2, product_3])
    assert product.name == "Iphone 15"
    assert product.price == 210000.0
    assert product.quantity == 13


def test_price(product_1, capsys):
    old_price = product_1.price
    product_1.price = -100
    assert product_1.price == old_price
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    product_1.price = 0
    assert product_1.price == old_price
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    product_1.price = old_price + 100
    assert product_1.price == old_price + 100


@patch("src.product.confirm")
def test_price_setter_decrease_confirmed(mock_confirm, product_1, capsys):
    mock_confirm.return_value = True
    product_1.price = 100000.0
    assert product_1.price == 100000.0
    captured = capsys.readouterr()
    assert "Действие выполнено" in captured.out


@patch("src.product.confirm")
def test_price_setter_decrease_cancelled(mock_confirm, product_1, capsys):
    mock_confirm.return_value = False
    old_price = product_1.price
    product_1.price = 100000.0
    assert product_1.price == old_price
    captured = capsys.readouterr()
    assert "Действие отменено" in captured.out


def test_product_str(product_1):
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_1, product_2):
    res = product_1 + product_2
    assert res == 2580000.0


def test_product_add_type_err(product_1):
    with pytest.raises(TypeError):
        _ = product_1 + 1000
