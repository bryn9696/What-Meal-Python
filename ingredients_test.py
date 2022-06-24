from ingredients import Ingredients

def test_ingredients() -> None:
  assert Ingredients.ingredients(["HAM"]) == (["Ham"])

def test_dictionary() -> None:
  assert Ingredients.dictionary(['Cheese']) == (["Cheese"])