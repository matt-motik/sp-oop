"""Модуль вспомогательных функций."""

import json
import os
from typing import Any

from src.category import Category
from src.logger_creator import create_logger
from src.path import get_data_dir
from src.product import Product

logger = create_logger(__name__)


def read_json_file(filename: str) -> Any | None:
    """Функция чтения JSON-файла.

    Args:
        filename: Путь к JSON-файлу.

    Returns:
        JSON объект или None в случае неудачи.

    Example:

        >>> result = read_json_file("data/products.json")
    """
    logger.debug(f"Проверка JSON-файла filename '{filename}' на существование")
    if filename:
        if os.path.exists(filename):
            logger.debug(f"JSON-файла '{filename}' существует")
            logger.debug(f"Открываем JSON-файл '{filename}' на чтение")
            with open(filename, "r", encoding="utf-8") as f:
                try:
                    logger.debug("Читаем JSON-файл'")
                    result = json.load(f)
                    return result
                except json.JSONDecodeError as err:
                    logger.warning(f"Данные не являются корректным JSON. Возвращаем None. {str(err)}", exc_info=True)
                    return None

    logger.warning("Файл не указан. Возвращаем None")
    return None


def create_categories_from_json(filename: str) -> list[Category]:
    """Создаёт список категорий из JSON-файла.

    Args:
        filename: Имя JSON-файла в директории data/.

    Returns:
        Список объектов Category или пустой список при ошибке.

    Example:

        >>> result = create_categories_from_json("products.json")
    """
    logger.info("Получаем данные о категориях из файла.")
    datadir = get_data_dir()
    json_data = read_json_file(os.path.join(datadir, filename))
    if json_data is None:
        return []

    if not isinstance(json_data, list):
        logger.error(f"Ожидался список, получено: {type(json_data).__name__}")
        return []

    categories = []

    for category in json_data:
        try:
            category["products"] = [Product(**p) for p in category.get("products", [])]
            categories.append(Category(**category))
        except (TypeError, KeyError, ValueError, AttributeError) as err:
            logger.error(f"Данные не являются корректным представлением категории. {str(err)}", exc_info=True)
    logger.info("Возвращаем список категорий.")
    return categories
