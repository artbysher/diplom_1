import allure

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestsDataBase:
    @allure.title("Тест инициализации атрибутов")
    def test_init_burger(self):
        db = Database()
        assert len(db.buns) == 3 and len(db.ingredients) == 6


    @allure.title("Тест возвращения корректного списка булочек после инициализации")
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert  len(buns) == 3 and [bun.get_name() for bun in buns] == ["black bun", "white bun","red bun"]

    @allure.title("Тест возвращения корректного списка ингредиентов после инициализации")
    def test_available_buns(self):
        db = Database()
        ingredients = db.available_ingredients()

        sauce_names = [ingredients.get_name() for ingredients in ingredients if ingredients.get_type() == INGREDIENT_TYPE_SAUCE]
        filling_names = [ingredients.get_name() for ingredients in ingredients if ingredients.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(ingredients) == 6 and sauce_names == ["hot sauce", "sour cream", "chili sauce"] and filling_names == ["cutlet", "dinosaur", "sausage"]