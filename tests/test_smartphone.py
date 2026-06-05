from unittest.mock import patch

import pytest

from src.smartphone import Smartphone


def test_smartphone_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_smartphone_add(smartphone_1, smartphone_2):
    res = smartphone_1 + smartphone_2
    assert res == 2580000.0


def test_smartphone_add_type_err(grass_1, smartphone_1):
    with pytest.raises(TypeError):
        _ = smartphone_1 + grass_1