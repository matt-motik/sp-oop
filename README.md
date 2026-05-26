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
- [ ] `utils.py` — чтение Json-файла
- [ ] `product.py` — Класс Продуктов
- [ ] `category.py` — Класс Категорий продуктов
- [ ] Тесты ко всем модулям (`utils`, `product`, `category`)
- [ ] Логирование
- [ ] `.env` и `.env.example`
- [ ] Финальная вычитка документации и обновление README
- [ ] Обновить документацию

## Команда проекта
- Matvey Bakirov — [mabakirov@gmail.com](mailto:mabakirov@gmail.com) — Back-End Engineer
 