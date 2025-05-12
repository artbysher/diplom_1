import allure


from praktikum.ingredient import Ingredient


class TestIngredient:
    @allure.title("Тест инициализации атрибутов ingredient_type, name и price в классе Ingredient")
    def test_init_ingredient_type_name_and_price(self):
        ingredient = Ingredient("Соус","Жижа", 300.0)
        assert ingredient.type =="Соус" and  ingredient.name == "Жижа" and ingredient.price == 300

    @allure.title("Тест на верное присвоение типа ингридиента ")
    def test_init_ingredient_type_name_and_price(self):
        ingredient = Ingredient("Соус", "Жижа", 300.0)
        assert ingredient.get_type() == "Соус"

    @allure.title("Тест на возвращение правильного названия, после присвоения")
    def  test_get_name_ingredient_returns_correct_name(self):
        ingredient = Ingredient("Соус","Жижа", 300.0)
        assert ingredient.get_name() == "Жижа"

    @allure.title("Тест ожидаем тип строка, а получаем список ")
    def test_get_name_ingredient_not_str(self):
        ingredient = Ingredient("Соус",100, 300.0)
        assert not isinstance(ingredient.get_name(), str)

    @allure.title("Тест на корректное присвоение цены")
    def test_get_price_ingredient_returns_correct_price(self):
        ingredient = Ingredient("Соус","Жижа", 300.0)
        assert ingredient.get_price() == 300

    @allure.title("Тест на корректное создание бесплатной булочки")
    def test_get_price_ingredient_returns_zero_price(self):
        ingredient = Ingredient("Соус","Жижа", 0)
        assert ingredient.get_price() == 0

    @allure.title("Тест ожидали  тип float, но получили строку")
    def test_get_price_ingredient_not_float(self):
        ingredient = Ingredient("Соус","Жижа", "300")
        assert not isinstance(ingredient.get_price(), float)
