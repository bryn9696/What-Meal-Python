from ingredients import ingredients

  # it 'returns inputted ingredient' do
  #   expect(Ingredients.ingredients(["Cheese"])).to eq(['Cheese'])
  # end
def test_ingredients() -> None:
  assert ingredients(["Ham"]) != (["Ham"])
