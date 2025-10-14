from pytest import fixture
from mcpacker.model.datapack.recipe.shapelessrecipe import ShapelessRecipe


# Fixtures #########################################################################################

@fixture(name="recipe")
def createRecipe():
    yield ShapelessRecipe("flint_and_steel", ["iron_ingot", "flint"], "flint_and_steel")


# Tests ############################################################################################

def test_recipe(recipe:ShapelessRecipe):
    assert ", ".join(str(i) for i in recipe.ingredients) == "minecraft:iron_ingot, minecraft:flint"
    assert str(recipe.resultId) == "minecraft:flint_and_steel"
    assert recipe.resultCount == 1
