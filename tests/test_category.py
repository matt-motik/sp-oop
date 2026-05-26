from src.category import Category
from src.product import Product


def test_init(category_1):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.products[0].name == "Samsung Galaxy S23 Ultra"
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
    assert category.products == []
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
