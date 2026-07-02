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
| [**`base_container.py`**](docs/api/base_container.md) | | |
| | [📦 BaseContainer](docs/api/base_container.md#BaseContainer) | Абстрактный класс для сущностей, содержащих товары и имеющих общую стоимость. |
| | [⚙️ BaseContainer.total_price](docs/api/base_container.md#BaseContainer.total_price) | Общая стоимость всех товаров в контейнере. |
| | [🔧 total_price](docs/api/base_container.md#total_price) | Общая стоимость всех товаров в контейнере. |
| [**`base_product.py`**](docs/api/base_product.md) | | |
| | [📦 BaseProduct](docs/api/base_product.md#BaseProduct) | Базовый абстрактный класс продукта. |
| | [⚙️ BaseProduct.price](docs/api/base_product.md#BaseProduct.price) | Геттер для получения цены продукта. |
| | [⚙️ BaseProduct.price](docs/api/base_product.md#BaseProduct.price) | Сеттер для установки или обновления цены продукта. |
| | [🔧 price](docs/api/base_product.md#price) | Геттер для получения цены продукта. |
| | [🔧 price](docs/api/base_product.md#price) | Сеттер для установки или обновления цены продукта. |
| [**`category.py`**](docs/api/category.md) | | |
| | [📦 Category](docs/api/category.md#Category) | Класс, представляющий категорию продуктов. |
| | [⚙️ Category.add_product](docs/api/category.md#Category.add_product) | Добавляет продукт в приватный список товаров категории. |
| | [⚙️ Category.products](docs/api/category.md#Category.products) | Возвращает отформатированную строку со списком товаров категории. |
| | [⚙️ Category.products_list](docs/api/category.md#Category.products_list) | Возвращает список товаров категории. |
| | [⚙️ Category.total_price](docs/api/category.md#Category.total_price) | Общая стоимость всех товаров в категории. |
| | [⚙️ Category.average_price](docs/api/category.md#Category.average_price) | Средняя стоимость всех товаров в категории. |
| | [🔧 add_product](docs/api/category.md#add_product) | Добавляет продукт в приватный список товаров категории. |
| | [🔧 products](docs/api/category.md#products) | Возвращает отформатированную строку со списком товаров категории. |
| | [🔧 products_list](docs/api/category.md#products_list) | Возвращает список товаров категории. |
| | [🔧 total_price](docs/api/category.md#total_price) | Общая стоимость всех товаров в категории. |
| | [🔧 average_price](docs/api/category.md#average_price) | Средняя стоимость всех товаров в категории. |
| [**`category_iterator.py`**](docs/api/category_iterator.md) | | |
| | [📦 CategoryIterator](docs/api/category_iterator.md#CategoryIterator) | Итератор для безопасного перебора товаров в категории. |
| [**`exceptions.py`**](docs/api/exceptions.md) | | |
| | [📦 QuantityError](docs/api/exceptions.md#QuantityError) | Класс, представляющий исключения при попытке добавить продукт с нулевым количеством. |
| [**`lawn_grass.py`**](docs/api/lawn_grass.md) | | |
| | [📦 LawnGrass](docs/api/lawn_grass.md#LawnGrass) | Класс, представляющий Траву газонную. |
| [**`logger_creator.py`**](docs/api/logger_creator.md) | | |
| | [🔧 create_logger](docs/api/logger_creator.md#create_logger) | Функция для создания логгера. |
| [**`order.py`**](docs/api/order.md) | | |
| | [📦 Order](docs/api/order.md#Order) | Класс, представляющий заказ на один товар. |
| | [⚙️ Order.total_price](docs/api/order.md#Order.total_price) | Итоговая стоимость заказа. |
| | [🔧 total_price](docs/api/order.md#total_price) | Итоговая стоимость заказа. |
| [**`path.py`**](docs/api/path.md) | | |
| | [🔧 get_log_path](docs/api/path.md#get_log_path) | Функция для получения пути к папке с логами. |
| | [🔧 get_root_dir](docs/api/path.md#get_root_dir) | Функция для получения пути к корневой папке проекта. |
| | [🔧 get_data_dir](docs/api/path.md#get_data_dir) | Функция для получения пути к папке с данными. |
| [**`print_mixin.py`**](docs/api/print_mixin.md) | | |
| | [📦 ProductProtocol](docs/api/print_mixin.md#ProductProtocol) | Протокол для миксина. |
| | [📦 PrintMixin](docs/api/print_mixin.md#PrintMixin) | Класс, представляющий Репрезентацию экземпляра. |
| [**`product.py`**](docs/api/product.md) | | |
| | [📦 Product](docs/api/product.md#Product) | Класс, представляющий продукт. |
| | [⚙️ Product.new_product](docs/api/product.md#Product.new_product) | Создаёт экземпляр Product из словаря или обновляет существующий товар. |
| | [⚙️ Product.price](docs/api/product.md#Product.price) | Геттер для получения цены продукта. |
| | [⚙️ Product.price](docs/api/product.md#Product.price) | Сеттер для установки или обновления цены продукта. |
| | [🔧 new_product](docs/api/product.md#new_product) | Создаёт экземпляр Product из словаря или обновляет существующий товар. |
| | [🔧 price](docs/api/product.md#price) | Геттер для получения цены продукта. |
| | [🔧 price](docs/api/product.md#price) | Сеттер для установки или обновления цены продукта. |
| [**`smartphone.py`**](docs/api/smartphone.md) | | |
| | [📦 Smartphone](docs/api/smartphone.md#Smartphone) | Класс, представляющий Смартфоны. |
| [**`utils.py`**](docs/api/utils.md) | | |
| | [🔧 read_json_file](docs/api/utils.md#read_json_file) | Функция чтения JSON-файла. |
| | [🔧 create_categories_from_json](docs/api/utils.md#create_categories_from_json) | Создаёт список категорий из JSON-файла. |
| | [🔧 confirm](docs/api/utils.md#confirm) | Запрашивает у пользователя подтверждение действия через консоль. |

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
src/__init__.py                0      0   100%
src/base_container.py          3      0   100%
src/base_product.py            4      0   100%
src/category.py               54      0   100%
src/category_iterator.py      17      0   100%
src/exceptions.py              6      0   100%
src/lawn_grass.py             13      0   100%
src/logger_creator.py         15      0   100%
src/order.py                  30      0   100%
src/path.py                   10      0   100%
src/print_mixin.py             7      0   100%
src/product.py                45      0   100%
src/smartphone.py             14      0   100%
src/utils.py                  52      0   100%
TOTAL                        270      0   100%
Coverage HTML written to dir htmlcov/src

🎯 Результаты тестов src:
tests/test_base_product.py .                                             [  1%]
tests/test_category.py .............                                     [ 25%]
tests/test_category_iterator.py ..                                       [ 28%]
tests/test_lawn_grass.py ...                                             [ 33%]
tests/test_logger_creator.py ..                                          [ 37%]
tests/test_order.py ....                                                 [ 44%]
tests/test_path.py ...                                                   [ 50%]
tests/test_print_mixin.py .                                              [ 51%]
tests/test_product.py ...........                                        [ 71%]
tests/test_smartphone.py ...                                             [ 76%]
tests/test_utils.py .............                                        [100%]
================================ tests coverage ================================
--------------------------------------------------------
--------------------------------------------------------
============================== 56 passed in 0.13s ==============================
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
- [x] Логирование важных функций
- [x] Атрибут `products` в `Category` сделать приватным (`__products`)
- [x] Реализовать метод `add_product()` для безопасного добавления товаров
- [x] Реализовать геттер `@property products`, должен возвращать строку в формате: `"Название, X руб. Остаток: X шт.\n"`
- [x] Реализовать класс-метод `Product.new_product()`, должен создавать объект из `dict`, поддерживать слияние дубликатов (сумма `quantity`, выбор `max(price)`)
- [x] Приватизировать цену `Product`  (`__price`), реализовать геттер/сеттер
- [x] Сеттер должен `price` валидировать `>0`, выводить предупреждение при `<=0`, запрашивать подтверждение при снижении цены
- [x] Переопределить `__str__` в `Product` (формат: "Название, X руб. Остаток: X шт.")
- [x] Переопределить `__str__` в `Category` (формат: "Название, количество продуктов: X шт.", сумма quantity)
- [x] Переопределить `__add__` в `Product` для расчёта общей стоимости склада с проверкой типа
- [x] Создать вспомогательный класс `CategoryIterator` с методами `__iter__` и `__next__`
- [x] Создать классы-наследники `Smartphone` и `LawnGrass` с расширенными атрибутами
- [x] Доработать сложение (`__add__`): можно складывать только объекты одинаковых классов, иначе выбрасывается `TypeError` (используется `type()`)
- [x] Доработать метод `add_product`: нельзя добавить объект, не являющийся `Product` или его наследником (используется `isinstance()`, выбрасывается `TypeError`)
- [x] Реализован абстрактный класс `BaseProduct` и класс-миксин `PrintMixin` с множественным наследованием в `Product`
- [x] Создан абстрактный класс `BaseContainer`, от которого наследуют `Category` и новый класс `Order`
- [x] Реализована валидация количества при создании Product: при quantity <= 0 выбрасывается ValueError
- [x] В Category добавлен метод average_price() с обработкой ZeroDivisionError (возвращает 0)
- [x] Создан пользовательский класс исключения QuantityError
- [x] QuantityError используется в Category.add_product() и Order с блоками try/except/else/finally
- [x] Добавлено логирование и вывод сообщений при добавлении товаров в категорию и заказ
- [x] Исправить старые тесты с учётом изменений
- [x] Написать тесты для всей новой функциональности
- [x] Проверить линтеры (`flake8`, `mypy`, `pydocstyle`, `black`, `isort`)
- [x] Финальная вычитка документации и обновление README
- [x] Обновить документацию

## Команда проекта
- Matvey Bakirov — [mabakirov@gmail.com](mailto:mabakirov@gmail.com) — Back-End Engineer
 