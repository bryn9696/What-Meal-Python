class Recipes:
  
  options = []
  def __init__(self):
	  self.options = []

  def cheese_toasty_dish(self, ingredients_list):
    # options = []
    cheese_toasty = ['Cheese', 'Bread', 'Butter']
    for i in ingredients_list:
      if i in cheese_toasty:
        self.options.append(f"Cheese Toasty: {', '.join(cheese_toasty)}")
    return self.options
