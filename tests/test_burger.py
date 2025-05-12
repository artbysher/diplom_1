import pytest
import allure
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestsBurger:
    @allure.title("Тест инициализации атрибутов, проверяем что после создания объякта булочка и ингридиенты не заданы")
    def test_init_burger(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    @allure.title("Тест на корректное присповение объекта булочка")
    def test_set_buns_positive(self):
        burger = Burger()
        bun = Bun("Чудо булка",3000)
        burger.set_buns(bun)
        assert burger.bun == bun and burger.bun.name == "Чудо булка"

    @allure.title("Тест на корректное обновление повторно заданного объекта булочка")
    def test_set_buns_replace_bun(self):
        burger = Burger()
        bun1 = Bun("Чудо булка",3000)
        bun2 = Bun("Мегабулка",2000)
        burger.set_buns(bun1)
        burger.set_buns(bun2)
        assert burger.bun == bun2 and burger.bun.name == "Мегабулка"

    @allure.title("Тест на возможность убрать булку из бургера")
    def test_set_buns_none(self):
        burger = Burger()
        bun = Bun("Чудо булка", 3000)
        burger.set_buns(bun)
        burger.set_buns(None)
        assert burger.bun is None

    @allure.title("Тест на успешное добавление ингридиента")
    def test_add_ingredient_to_list(self):
        burger = Burger()
        ingredient = Ingredient("FILLING", "Сыр", 300)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient

    @allure.title("Тест на добавление нескольких ингредиентов, каждый следующий добавляется в конец списка")
    def test_add_ingredients_append_multiple(self):
        burger = Burger()
        ingredient1 = Ingredient("FILLING","Сыр", 300)
        ingredient2 = Ingredient("FILLING","Помидор",300)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert len(burger.ingredients) == 2 and burger.ingredients == [ingredient1, ingredient2]

    @allure.title("Тест на добавление данных типа строка вместо списка, подтверждение уязвимости метода add_ingredient")
    def test_add_ingredient_wrong_type(self):
        burger = Burger()
        ingredient = Ingredient("FILLING", "Сыр", 300)
        burger.add_ingredient(ingredient)
        bad_data = "Не ингредиент"
        burger.add_ingredient(bad_data)
        assert not all(isinstance(i, Ingredient) for i in burger.ingredients) and len(burger.ingredients) == 2

    @allure.title("Тест на удаление единственного ингредиента")
    def test_remove_ingredient_singal_index(self):
        burger = Burger()
        ingredient = Ingredient("FILLING", "Сыр", 300)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @allure.title("Тест на удаление ингредиента по индексу ")
    def test_remove_ingredient_for_index(self):
        burger = Burger()
        ingredient1 = Ingredient("FILLING", "Сыр", 300)
        ingredient2 = Ingredient("FILLING", "Огурчик", 300)
        ingredient3 = Ingredient("FILLING", "Грибочки", 300)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.remove_ingredient(2)
        assert len(burger.ingredients) == 2 and [i.name for i in burger.ingredients] == ["Сыр", "Огурчик"]


    @allure.title("Тест на удаление не существующего ингредиента ")
    def test_remove_ingredient_nonexistent_index(self):
        burger = Burger()
        ingredient1 = Ingredient("FILLING", "Сыр", 300)
        ingredient2 = Ingredient("FILLING", "Огурчик", 300)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        with pytest.raises(IndexError):
            burger.remove_ingredient(2)
        assert [i.name for i in burger.ingredients] == ["Сыр", "Огурчик"]

    @allure.title("Тест на удаление из пустого списка ")
    def  test_remove_ingredient_empty_list(self):
        burger = Burger()

        with pytest.raises(IndexError):
            burger.remove_ingredient(0)
        assert burger.ingredients == []


    @allure.title("Тест перемещение ингредиента внутри списка ")
    def test_move_ingredient_inside_list(self):
        burger = Burger()
        ingredient1 = Ingredient("FILLING", "Сыр", 300)
        ingredient2 = Ingredient("FILLING", "Огурчики", 300)
        ingredient3 = Ingredient("FILLING", "Грибочки", 300)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0,2)
        assert (len(burger.ingredients) == 3
                and [i.name for i in burger.ingredients] == ['Огурчики', 'Грибочки', 'Сыр'])

    @allure.title("Тест перемещение ингредиента на ту же позицию в списке ")
    def test_move_ingredient_same_place(self):
        burger = Burger()
        ingredient1 = Ingredient("FILLING", "Сыр", 300)
        ingredient2 = Ingredient("FILLING", "Огурчики", 300)
        ingredient3 = Ingredient("FILLING", "Грибочки", 300)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        original_list = burger.ingredients.copy()
        burger.move_ingredient(1,1)
        assert len(burger.ingredients) == 3 and burger.ingredients == original_list


    @allure.title("Тест на перемещение не существующего ингредиента ")
    def test_move_ingredient_nonexistent_index(self):
        burger = Burger()
        ingredient1 = Ingredient("FILLING", "Сыр", 300)
        ingredient2 = Ingredient("FILLING", "Огурчик", 300)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        with pytest.raises(IndexError):
            burger.move_ingredient(2,0)

        assert [i.name for i in burger.ingredients] == ["Сыр", "Огурчик"]

    @allure.title("Тест перемещение внути пустого списка ")
    def  test_move_ingredient_empty_list(self):
        burger = Burger()

        with pytest.raises(IndexError):
            burger.move_ingredient(0,0)
        assert burger.ingredients == []


    @allure.title("Тест на правильный подсчет цены бургера")
    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 1000.0
        burger.bun = bun_mock

        ingredient1 = Mock()
        ingredient1.get_price.return_value = 500.0
        ingredient2 = Mock()
        ingredient2.get_price.return_value = 300.0
        burger.ingredients = [ingredient1, ingredient2]

        expected_price = 1000.0 * 2 + 500.0 + 300.0
        assert burger.get_price() == expected_price

    @allure.title("Тест создание текстового чека с одним ингридиентом")
    def test_get_receipt_single_ingredient(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Экстра булка"
        burger.bun = bun_mock

        ingredient_mock = Mock()
        ingredient_mock.get_type.return_value = "Sauce"
        ingredient_mock.get_name.return_value = "Горчица"
        burger.ingredients = [ingredient_mock]

        burger.get_price = Mock(return_value=2500.5)

        expected = "(==== Экстра булка ====)\n= sauce Горчица =\n(==== Экстра булка ====)\n\nPrice: 2500.5"
        assert burger.get_receipt() == expected

    @allure.title("Тест создание текстового чека с одним ингридиентом")
    def test_get_receipt_no_ingredient(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Бесячая булка"
        burger.bun = bun_mock

        burger.ingredients = []

        burger.get_price = Mock(return_value=3000.0)

        expected = "(==== Бесячая булка ====)\n(==== Бесячая булка ====)\n\nPrice: 3000.0"
        assert burger.get_receipt() == expected