# SkyPro Модуль ООП
Учебный проект. Представляет собой частичную реализацию для интернет-магазина.
### 🚀 Возможности программы

- **Источник данных** — загрузка из JSON файлов


## Содержание
- [Технологии](#технологии)
- [Установка](#установка)
- [Разработка](#разработка)
- [Тестирование](#тестирование)
- [Deploy и CI/CD](#deploy-и-cicd)
- [Contributing](#contributing)
- [FAQ](#faq)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)


<div id="технологии"></div>

## Технологии
- [Python](https://www.python.org/)
- [pytest](https://docs.pytest.org/) — тестирование с покрытием
- [poetry](https://python-poetry.org/) — управление зависимостями

[//]: # (- [yfinance]&#40;https://pypi.org/project/yfinance/&#41; — получение цен акций)
[//]: # (- [questionary]&#40;https://pypi.org/project/questionary/&#41; — интерактивное меню)
[//]: # (- [pandas]&#40;https://pandas.pydata.org/&#41; — обработка Excel файлов)
[//]: # (- [requests]&#40;https://docs.python-requests.org/&#41; — HTTP-запросы к API конвертации валют)

<div id="установка"></div>

## Установка
Для управления зависимостями в проекте используется [Poetry](https://python-poetry.org).

1. Клонируйте репозиторий:
```
git clone https://github.com/matt-motik/sp-oop.git
cd sp-oop
poetry install
```

<div id="разработка"></div>

## Разработка
<!-- СЕКЦИЯ_AUTO_API: СТАРТ -->
### 📚 Документация API

*Этот раздел генерируется автоматически из docstring.*

| Модуль | Функция/Класс | Краткое описание |
|--------|---------------|------------------|
| [**`category.py`**](docs/api/category.md) | | |
| | [📦 Category](docs/api/category.md#Category) | Класс, представляющий категорию продуктов. |
| [**`logger_creator.py`**](docs/api/logger_creator.md) | | |
| | [🔧 create_logger](docs/api/logger_creator.md#create_logger) | Функция для создания логгера. |
| [**`path.py`**](docs/api/path.md) | | |
| | [🔧 get_log_path](docs/api/path.md#get_log_path) | Функция для получения пути к папке с логами. |
| | [🔧 get_root_dir](docs/api/path.md#get_root_dir) | Функция для получения пути к корневой папке проекта. |
| | [🔧 get_data_dir](docs/api/path.md#get_data_dir) | Функция для получения пути к папке с данными. |
| [**`product.py`**](docs/api/product.md) | | |
| | [📦 Product](docs/api/product.md#Product) | Класс, представляющий продукт. |
| [**`utils.py`**](docs/api/utils.md) | | |
| | [🔧 read_json_file](docs/api/utils.md#read_json_file) | Функция чтения JSON-файла. |
| | [🔧 create_categories_from_json](docs/api/utils.md#create_categories_from_json) | Создаёт список категорий из JSON-файла. |

> 📘 **Полная документация** с примерами и описанием параметров доступна в папке [`docs/api`](docs/api).

<!-- СЕКЦИЯ_AUTO_API: КОНЕЦ -->
### Требования
В разработке
### Установка зависимостей
```poetry install```
### Запуск программы
```poetry run python src/main.py```
### Создание билда
В разработке

<div id="тестирование"></div>

## 🧪 Тестирование
main.py не тестируется
<!-- СЕКЦИЯ_AUTO_TEST: СТАРТ -->

*Этот раздел генерируется автоматически на основании данных `poetry run pytest`.*

### 📊 Результаты тестов SRC

```
📈 Покрытие кода:
tests/test_category.py .....                                             [ 22%]
tests/test_logger_creator.py ..                                          [ 31%]
tests/test_path.py ...                                                   [ 45%]
tests/test_product.py .                                                  [ 50%]
tests/test_utils.py ...........                                          [100%]
src/__init__.py             0      0   100%
src/category.py            10      0   100%
src/logger_creator.py      15      0   100%
src/path.py                10      0   100%
src/product.py              6      0   100%
src/utils.py               42      0   100%
TOTAL                      83      0   100%
Coverage HTML written to dir htmlcov/src

🎯 Результаты тестов src:
============================= test session starts ==============================
tests/test_category.py .....                                             [ 22%]
tests/test_logger_creator.py ..                                          [ 31%]
tests/test_path.py ...                                                   [ 45%]
tests/test_product.py .                                                  [ 50%]
tests/test_utils.py ...........                                          [100%]
================================ tests coverage ================================
-----------------------------------------------------
-----------------------------------------------------
============================== 22 passed in 0.08s ==============================
```

> 📊 **HTML отчёт покрытия**: [`htmlcov/index.html`](htmlcov/src/index.html)



<!-- СЕКЦИЯ_AUTO_TEST: КОНЕЦ -->
## Deploy и CI/CD
В разработке


## Contributing
В разработке — [Contributing.md](./CONTRIBUTING.md).

## FAQ
В разработке

## To do
- [x] Структура проекта, `pyproject.toml`, `README.md`, `.gitignore`
- [x] Виртуальное окружение, установка зависимостей через Poetry
- [x] `readme_gen.py` — скрипт генерации README, и покрытия тестами
- [x] `lint.ps1` — скрипт литеров, форматеров, типизаторов и др
- [x] `main.py` — проверка работоспособности классов
- [x] `utils.py` — чтение Json-файла
- [x] `product.py` — Класс Продуктов
- [x] `category.py` — Класс Категорий продуктов
- [x] Тесты ко всем модулям (`utils`, `product`, `category`)
- [x] Логирование важных функций
- [x] Финальная вычитка документации и обновление README
- [x] Обновить документацию

## Команда проекта
- Matvey Bakirov — [mabakirov@gmail.com](mailto:mabakirov@gmail.com) — Back-End Engineer
 