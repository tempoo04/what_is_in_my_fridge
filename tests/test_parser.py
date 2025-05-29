from app.core.parser import IngredientParser

def test_ingredientparser():
    assert IngredientParser.parse("apples and bananas") == ["apple", "banana"]
    assert IngredientParser.parse("organic milk") == ["organic", "milk"]