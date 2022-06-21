from recipes import Recipes

def test_cheese_toasty() -> None:
  r = Recipes
  assert r.cheese_toasty(["Cheese"]) == (["Cheese Toasty: Cheese, Bread, Butter"])