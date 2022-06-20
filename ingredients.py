def ingredients(ingredient_list):
  ing_list = []
  
  for ing in ingredient_list:
    s = str(ing)
    lc = s.lower()
    c = lc.capitalize()
    ing_list.append(c)
  print(ing_list)


print(ingredients)
