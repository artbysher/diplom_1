import allure
import pytest

from praktikum.bun import Bun


class TestBun:
    @allure.title("Тест инициализации атрибутов name и price в классе Bun")
    def test_name_and_price(self):
        bun = Bun("Бодробулка", 3000.0)
        assert bun.name == "Бодробулка" and bun.price == 3000

    @allure.title("Тест на возвращение правильного названия, после присвоения")
    def  test_get_name_returns_correct_name(self):
        bun = Bun("Бодробулка", 3000.0)
        assert bun.get_name() == "Бодробулка"

    @allure.title("Тест ожидаем тип строка в названии, а получаем список ")
    def test_get_name_not_str(self):
        bun = Bun(["Бубулка","Хахабулка"], 3000)
        assert not isinstance(bun.get_name(), str)

    @allure.title("Тест на корректное присвоение цены")
    def test_get_price_returns_correct_price(self):
        bun = Bun("Бодробулка", 3000.0)
        assert bun.get_price() == 3000

    @allure.title("Тест на корректное создание бесплатной булочки")
    def test_get_price_returns_zero_price(self):
        bun = Bun("Подарочная", 0)
        assert bun.get_price() == 0

    @allure.title("Тест ожидали  тип float, но получили строку")
    def test_get_price_not_float(self):
        bun = Bun("Бесячая булка", "десять")
        assert not isinstance(bun.get_price(), float)
