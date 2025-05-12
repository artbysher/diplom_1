## Дипломный проект. Задание 1: Юнит-тесты
<hr>

## Студент: Александра Шеремет

## <h>Когорта: #17</h>
<hr>

## <h>Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results

### <h>4.Запуск автотестов и создание HTML-отчета о покрытии </h>

>  `$ pytest --cov=praktikum --cov-report=html`
> 
### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 99% 
>(отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. `test_bun.py`, `test_burger.py`, `test_database.py`, `test_ingredient.py`


<hr>

