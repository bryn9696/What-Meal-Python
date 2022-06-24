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
    print(len(spell_check))
    for x in spell_check:
      for i in range(0, len(ingredients_list), 1):
        if 1<2: 
          print('he', i)
          ingredients_list.pop(i)
          ingredients_list.insert(i, str(spell_check[i]))
          print(ingredients_list)
          print('hello', i)
          # i = i+1
        print(i)
    print(ingredients_list)
    return ingredients_list
    # for ing in spell_check:
    #   i = 0
    #   if ing.chars().sort == ingredients_list[i].chars().sort():
    #     ingredients_list.delete(ingredients_list[i])
    #     ingredients_list << ing
    #   i += 1
    # print(recipes)
    # ingredients_list.uniq.sort

  def choice(ingredients_list):
    Recipes.new.choices(ingredients_list)
