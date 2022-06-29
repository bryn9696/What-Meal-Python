from ingredients import Ingredients

def test_ingredients() -> None:
  assert Ingredients.ingredients(["HAM"]) == (["Ham"])

def test_dictionary() -> None:
  assert Ingredients.dictionary(['Cheese']) == (["Cheese"])

def test_dictionary_one_item_not_first_in_spellcheck() -> None:
  assert Ingredients.dictionary(['Bread']) == (["Bread"])

# def test_dictionary_one_item_not_spelt_correctly_in_spell_check() -> None:
#   assert Ingredients.dictionary(['Egg']) == ([""])

# def test_dictionary_one_item_not_spelt_correctly_in_spellcheck() -> None:
  # assert Ingredients.dictionary(['Che']) == (["Cheese"])

def test_dictionary_two_items_returns_alphabetically() -> None:
  assert Ingredients.dictionary(['Cheese', 'Bread']) == (['Bread', 'Cheese'])

def test_dictionary_two_items_different_order_returns_alphabetically() -> None:
  assert Ingredients.dictionary(['Bread', 'Cheese']) == (['Bread', 'Cheese'])