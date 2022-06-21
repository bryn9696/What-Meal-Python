from recipes import Recipes

def test_cheese_toasty() -> None:
  assert Recipes().cheese_toasty_dish(["Cheese"]) == (["Cheese Toasty: Cheese, Bread, Butter"])

def test_all_ingredients() -> None:
  assert Recipes().all_ingredients == (['Cheese', 'Bread', 'Butter', 'Ham'])

# def test_all_ingredients() -> None:
#   assert Recipes().all_ingredients() == (['Cheese', 'Bread', 'Butter', 'Ham'])