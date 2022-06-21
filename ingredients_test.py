from ingredients import Ingredients

def test_ingredients() -> None:
  i = Ingredients
  assert i.ingredients(["HAM"]) == (["Ham"])
