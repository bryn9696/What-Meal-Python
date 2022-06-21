from ingredients import Ingredients

def test_ingredients() -> None:
  assert Ingredients.ingredients(["HAM"]) == (["Ham"])
