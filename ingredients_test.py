from ingredients import Ingredients

def test_ingredients() -> None:
  assert Ingredients.ingredients(["HAM"]) == (["Ham"])

def test_dictionary() -> None:
  assert Ingredients.dictionary(['Cheese']) == (["Cheese"])

def test_dictionary_one_item_not_first_in_spellcheck() -> None:
  assert Ingredients.dictionary(['Bread']) == (["Bread"])

def test_dictionary_two_items() -> None:
  assert Ingredients.dictionary(['Cheese', 'Bread']) == (["Cheese", "Bread"])