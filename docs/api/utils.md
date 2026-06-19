# Модуль: `utils.py`

*Сгенерировано: 2026-06-19 15:48:04*

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

<div id="confirm"></div>

## confirm

**Тип:** function

**Кратко:** Запрашивает у пользователя подтверждение действия через консоль.

### Полная документация

```python
Запрашивает у пользователя подтверждение действия через консоль.

Args:
    prompt: Текст приглашения для ввода.

Returns:
    True при вводе 'y', 'yes', 'д' или 'да'.
    False при вводе 'n', 'no', 'н' или 'нет'.

Example:
    >>> # При вводе 'y' в консоль:
    >>> confirm("Сохранить изменения? (y/n): ")
    True
```

---

