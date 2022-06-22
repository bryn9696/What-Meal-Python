# import pytest
# import functools
from recipes import Recipes


def test_cheese_toasty_cheese() -> None:
  assert Recipes().cheese_toasty_dish(["Cheese"]) == (["Cheese Toasty: Cheese, Bread, Butter"])

def test_cheese_toasty_bread() -> None:
  assert Recipes().cheese_toasty_dish(["Bread"]) == (["Cheese Toasty: Cheese, Bread, Butter"])

def test_ham_sandwhich() -> None:
  assert Recipes().ham_sandwhich_dish(["Ham"]) == (['Ham Sandwhich: Ham, Bread, Butter'])

def test_all_ingredients() -> None:
  assert Recipes().all_ingredients() == (['Cheese', 'Bread', 'Butter', 'Ham'])

# def test_choices() -> None:
#   assert Recipes().choices(["Ham"]) == (["Cheese Toasty: Cheese, Bread, Butter"])