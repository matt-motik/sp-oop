import pytest

from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасывает счётчики категорий и продуктов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0

    yield  # тут выполнится тест

    # Выполнится после теста
    # в данном случае не обязательно. Но осталю на память, что так можно
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_1(product_1, product_3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_3],
    )


@pytest.fixture
def category_2(product_2):
    return Category(
        "Apple",
        "Смартфоны Apple",
        [product_2],
    )


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

@pytest.fixture
def grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")