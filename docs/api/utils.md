# Модуль: `utils.py`

*Сгенерировано: 2026-05-26 21:38:36*

---

<div id="read_json_file"></div>

## read_json_file

**Тип:** function

**Кратко:** Функция чтения JSON-файла.

### Полная документация

```python
Функция чтения JSON-файла.

Args:
    filename: Путь к JSON-файлу.

Returns:
    JSON объект или None в случае неудачи.

Example:

    >>> result = read_json_file("data/products.json")
```

---

<div id="create_categories_from_json"></div>

## create_categories_from_json

**Тип:** function

**Кратко:** Создаёт список категорий из JSON-файла.

### Полная документация

```python
Создаёт список категорий из JSON-файла.

Args:
    filename: Имя JSON-файла в директории data/.

Returns:
    Список объектов Category или пустой список при ошибке.

Example:

    >>> result = create_categories_from_json("products.json")
```

---

