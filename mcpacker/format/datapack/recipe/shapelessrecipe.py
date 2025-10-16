from collections.abc                import Iterable
from collections.abc                import Mapping
from mcpacker.model.core.resourceid import ResourceId
from mcpacker.format.datapack.recipe import Recipe


# Class ############################################################################################

class ShapelessRecipe(Recipe):

    def __init__(
        self,
        gameId:str|ResourceId,
        ingredients:Iterable[str|ResourceId],
        resultId:str|ResourceId,
        resultCount:int=1,
        resultComponents:Mapping[str,str]|None=None,
    ):
        super().__init__(gameId, resultId, resultCount, resultComponents)
        self.ingredients = self._parseIngredients(ingredients)

    def _parseIngredients(self, ingredients:Iterable[str|ResourceId]) -> list[ResourceId]:
        result = [ ResourceId.parse(e) for e in ingredients ]

        if len(result) > 9:
            raise ValueError("cannot have more than 9 ingredients (\"{len(result}\" is not valid")

        return result
