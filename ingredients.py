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
    spell_check = recipes
    for x in spell_check:
      for i in range(0, len(ingredients_list), 1):
        # print(i, x)
        # print(ingredients_list[i] in x)
        if ingredients_list[i] in x == True: 
          ingredients_list.pop(i)
          ingredients_list.insert(i, str(x))
        # else:
    #       print("hi")
    # print(sorted(ingredients_list))
    return sorted(ingredients_list)

  def choice(ingredients_list):
    Recipes.new.choices(ingredients_list)
