"""Модуль вспомогательных функций."""
import json
import os
from typing import Any

from logger_creator import create_logger

logger = create_logger(__name__)

def read_json_file(filename: str) -> Any | None:
    """Функция чтения JSON-файла.

    Args:
        filename: Путь к JSON-файлу.

    Returns:
        JSON объект
        Если JSON-файл пустой, содержит не-список или не найден, возвращается None.

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