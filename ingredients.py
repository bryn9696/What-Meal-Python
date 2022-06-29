from recipes import Recipes

class Ingredients:
  def ingredients(ingredient_list):
    ing_list = []   
    for ing in ingredient_list:
      ing_string = str(ing).lower().capitalize()
      ing_list.append(ing_string)
      return ing_list

  def dictionary(ingredients_list):
    recipes = Recipes().all_ingredients()
    spell_check = sorted(recipes)
    ingredients_list = sorted(ingredients_list)
    for x in spell_check:
      for i in range(0, len(ingredients_list), 1):
        if ingredients_list[i].find(x) >= 0:
          ingredients_list.pop(i)
          ingredients_list.insert(i, str(x))
          print(ingredients_list)
          print(ingredients_list, '****')
    return ingredients_list

  def choice(ingredients_list):
    Recipes.new.choices(ingredients_list)
