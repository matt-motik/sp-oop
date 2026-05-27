import json
import os
import tempfile
from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product
from src.utils import create_categories_from_json
from src.utils import read_json_file


@pytest.mark.parametrize(
    "file_path, data, expected_result",
    [
        (None, None, None),
        ("", None, None),
        ("wrong/path.json", None, None),
        ("temp.json", "", None),
        ("temp.json", """{"answer": 42 }""", {"answer": 42}),
        ("temp.json", """Non JSON data, or error in JSON""", None),
        ("temp.json", """[ {"id": 0} , {}, {"id": 2} ]""", [{"id": 0}, {}, {"id": 2}]),
    ],
)
def test_read_json_file(file_path, data, expected_result):
    if file_path == "temp.json":
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_json = os.path.join(tmpdir, "temp.json")
            if data is not None:
                with open(temp_json, "w", encoding="utf-8") as f:
                    f.write(data)
            assert read_json_file(temp_json) == expected_result
    else:
        assert read_json_file(file_path) == expected_result


def test_create_categories_from_json_valid(tmp_path):
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Все смартфоны",
            "products": [{"name": "iPhone", "description": "Apple", "price": 1000.0, "quantity": 5}],
        }
    ]
    json_file = tmp_path / "products.json"
    json_file.write_text(json.dumps(test_data), encoding="utf-8")

    with patch("src.utils.get_data_dir", return_value=str(tmp_path)):
        categories = create_categories_from_json("products.json")

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"
    assert categories[0].product_count == 1
    assert categories[0].products == "iPhone, 1000.0 руб. Остаток: 5 шт.\n"


def test_create_categories_from_json_file_not_found(tmp_path):
    with patch("src.utils.get_data_dir", return_value=str(tmp_path)):
        categories = create_categories_from_json("nonexistent.json")

    assert categories == []


def test_create_categories_from_json_not_a_list(tmp_path):
    json_file = tmp_path / "products.json"
    json_file.write_text('{"not": "a list"}', encoding="utf-8")

    with patch("src.utils.get_data_dir", return_value=str(tmp_path)):
        categories = create_categories_from_json("products.json")

    assert categories == []


def test_create_categories_from_json_category_without_products(tmp_path):
    """Проверяет категорию без поля products."""
    test_data = [
        {"name": "Битая категория", "descript": "Вместо description"},
        {"name": "Пустая категория", "description": "Без продуктов"},
    ]
    json_file = tmp_path / "products.json"
    json_file.write_text(json.dumps(test_data), encoding="utf-8")

    with patch("src.utils.get_data_dir", return_value=str(tmp_path)):
        categories = create_categories_from_json("products.json")

    assert len(categories) == 1
    assert categories[0].products == ""
