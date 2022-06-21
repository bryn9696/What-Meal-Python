import functools
class Recipes:

  def __init__(self):
    self.options = []
    self.cheese_toasty = ['Cheese', 'Bread', 'Butter']
    self.ham_sandwhich = ['Ham', 'Bread', 'Butter']

  def all_ingredients(self):
    all_ing = self.cheese_toasty + self.ham_sandwhich
    all = list(dict.fromkeys(all_ing))
    return all

  def cheese_toasty_dish(self, ingredients_list):
    for i in ingredients_list:
      if i in self.cheese_toasty:
        self.options.append(f"Cheese Toasty: {', '.join(self.cheese_toasty)}")
    return self.options

  def ham_sandwhich_dish(self, ingredients_list):
    for i in ingredients_list:
      if i in self.ham_sandwhich:
        self.options.append(f"Ham Sandwhich: {', '.join(self.ham_sandwhich)}")
    return self.options

  def choices(self, ingredients_list):
    print(self.cheese_toasty_dish(ingredients_list))
