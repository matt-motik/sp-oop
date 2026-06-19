from unittest.mock import patch

import pytest

from src.lawn_grass import LawnGrass


def test_lawn_grass_init(grass_1):
    assert grass_1.name == "Газонная трава"
    assert grass_1.description == "Элитная трава для газона"
    assert grass_1.price == 500.0
    assert grass_1.quantity == 20
    assert grass_1.country == "Россия"
    assert grass_1.germination_period == "7 дней"
    assert grass_1.color == "Зеленый"


def test_lawn_grass_add(grass_1, grass_2):
    res = grass_1 + grass_2
    assert res == 16750.0

def test_lawn_grass_add_type_err(grass_1, smartphone_1):
    with pytest.raises(TypeError):
        _ = grass_1 + smartphone_1