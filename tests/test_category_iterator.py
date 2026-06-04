import pytest

from src.category_iterator import CategoryIterator
from src.product import Product


def test_category_iter(category_1):
    for product in CategoryIterator(category_1):
        assert isinstance(product, Product)

    iterator = CategoryIterator(category_1)
    for _ in range(len(category_1.products_list)):
        next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)


def test_category_iter_type_err():
    with pytest.raises(TypeError):
        _ = CategoryIterator("не категория")
