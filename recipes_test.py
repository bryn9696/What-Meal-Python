from recipes import Recipes

def test_cheese_toasty() -> None:
  r = Recipes()
  assert r.cheese_toasty_dish(["Cheese"]) == (["Cheese Toasty: Cheese, Bread, Butter"])