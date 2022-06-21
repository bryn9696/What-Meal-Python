class Recipes:


  def cheese_toasty(ingredients_list):
    options = []
    cheese_toasty = ['Cheese', 'Bread', 'Butter']
    for i in ingredients_list:
      if i in cheese_toasty:
        options.append("Cheese Toasty:")
    return options
