class Ingredients:
  def ingredients(ingredient_list):
    ing_list = []
    
    for ing in ingredient_list:
      ing_string = str(ing).lower().capitalize()
      ing_list.append(ing_string)
      return ing_list

