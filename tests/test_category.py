import pytest

from src.category import Category
from src.product import Product


def test_init(category_1):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации,"
        + " но и получения дополнительных функций для удобства жизни"
    )
    assert (
        category_1.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        + "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
    assert category_1.category_count == 1
    assert category_1.product_count == 2


def test_counters(category_1, category_2):
    assert category_1.category_count == 2
    assert category_1.product_count == 3
    assert category_2.category_count == 2
    assert category_2.product_count == 3


def test_category_with_empty_products():
    category = Category("Empty Category", "No products", [])
    assert category.name == "Empty Category"
    assert len(category.products) == 0
    assert category.product_count == 0


def test_category_with_none_products():
    category = Category("None Category", "None products", None)
    assert category.products == ""
    assert category.product_count == 0


def test_multiple_categories_counters():
    p1 = Product("P1", "D1", 10.0, 1)
    p2 = Product("P2", "D2", 20.0, 2)

    cat1 = Category("Cat1", "Desc1", [p1])
    assert Category.category_count == 1
    assert Category.product_count == 1
    assert cat1.category_count == 1
    assert cat1.product_count == 1

    cat2 = Category("Cat2", "Desc2", [p2])
    assert Category.category_count == 2
    assert Category.product_count == 2
    assert cat2.category_count == 2
    assert cat2.product_count == 2
    assert cat1.category_count == 2
    assert cat1.product_count == 2

    cat3 = Category("Cat3", "Desc3", [p1, p2])
    assert Category.category_count == 3
    assert Category.product_count == 4
    assert cat3.category_count == 3
    assert cat3.product_count == 4
    assert cat2.category_count == 3
    assert cat2.product_count == 4
    assert cat1.category_count == 3
    assert cat1.product_count == 4


def test_add_product_valid(category_1, product_2, caplog):
    old_count = category_1.product_count
    category_1.add_product(product_2)
    assert "Товар успешно добавлен" in caplog.text
    assert "Добавление завершено" in caplog.text

    assert category_1.product_count == old_count + 1
    assert product_2.name in category_1.products


def test_add_product_invalid(category_1, caplog):
    old_count = category_1.product_count
    category_1.add_product("это не продукт")
    assert "В категорию можно добавлять только объекты типа Product или его наследников" in caplog.text
    assert category_1.product_count == old_count


def test_category_str(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 19 шт."


def test_category_product_list(category_1):
    assert len(category_1.products_list) == 2
    assert all(isinstance(p, Product) for p in category_1.products_list)


def test_category_iter(category_1):
    for product in category_1:
        assert isinstance(product, Product)

    iterator = iter(category_1)
    for _ in range(len(category_1.products_list)):
        next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)


def test_category_total_price(category_1):
    assert category_1.total_price == sum(p.price * p.quantity for p in category_1.products_list)


def test_category_add_zero_quantity(category_1, product_1, caplog):
    product_1.quantity = 0
    category_1.add_product(product_1)
    assert "Товар с нулевым количеством не может быть добавлен" in caplog.text
    assert "Добавление завершено" in caplog.text


def test_category_average_price(category_empty, category_1, product_1, caplog):
    assert category_empty.average_price() == 0
    assert category_1.average_price() == 105500.0
