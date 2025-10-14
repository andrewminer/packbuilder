from pytest import fixture
from mcpacker.model.datapack.recipe.shapedrecipe import ShapedRecipe


# Fixtures #########################################################################################

@fixture(name="recipe")
def createRecipe():
    yield ShapedRecipe(
        "iron_pickaxe",
        {"s": "stick", "i": "iron_ingot"},
        ["iii", " s ", " s "],
        "iron_pickaxe"
    )


# Tests ############################################################################################

def test_recipe(recipe:ShapedRecipe):
    keyText = ", ".join(f"{k}:{str(v[0])}" for k,v in recipe.key.items())
    recipeText = "|".join(str(i) for i in recipe.pattern)

    assert keyText == "s:minecraft:stick, i:minecraft:iron_ingot"
    assert recipeText == "iii| s | s "
    assert str(recipe.resultId) == "minecraft:iron_pickaxe"
    assert recipe.resultCount == 1

