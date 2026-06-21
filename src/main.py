"""Основной модуль проекта."""

from .category import Category
from .product import Product

if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(e)
        print(
            "Возникла ошибка ValueError прерывающая работу"
            + "программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    prod1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    prod2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    prod3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [prod1, prod2])

    category1.add_product(prod3)

    print(category1.average_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.average_price())
