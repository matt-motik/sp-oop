"""Модуль вспомогательных функций."""

from __future__ import annotations

import json
import os
from typing import Any
from typing import TYPE_CHECKING

from .logger_creator import create_logger
from .path import get_data_dir

if TYPE_CHECKING:
    from .category import Category  # noqa: F401
    from .product import Product  # noqa: F401

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
    from .category import Category  # noqa: F811
    from .product import Product  # noqa: F811

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


def confirm(prompt: str = "Продолжить? (y/n): ") -> bool:
    """Запрашивает у пользователя подтверждение действия через консоль.

    Args:
        prompt: Текст приглашения для ввода.

    Returns:
        True при вводе 'y', 'yes', 'д' или 'да'.
        False при вводе 'n', 'no', 'н' или 'нет'.

    Example:
        >>> # При вводе 'y' в консоль:
        >>> confirm("Сохранить изменения? (y/n): ")
        True
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes", "д", "да"):
            return True
        elif answer in ("n", "no", "н", "нет"):
            return False
        else:
            print("Пожалуйста, введите 'y' (да) или 'n' (нет).")
