from collections.abc import Iterable
from collections.abc import Mapping
from mcpacker.model.datapack.recipe import Recipe
from mcpacker.model.core.resourceid import ResourceId


# Class ############################################################################################

class ShapedRecipe(Recipe):

    def __init__(
        self,
        gameId:str|ResourceId,
        key:Mapping[str,(str|ResourceId|Iterable[ResourceId|str])],
        pattern:Iterable[str],
        resultId:str|ResourceId,
        resultCount:int=1,
        resultComponents:Mapping[str,str]|None=None,
    ):
        super().__init__(gameId, resultId, resultCount, resultComponents)
        self.key = self._parseKey(key)
        self.pattern = self._parsePattern(pattern)

    # Private Methods ##########################################################

    def _parseKey(
        self,
        key:Mapping[str,(str|ResourceId|Iterable[ResourceId|str])]
    ) -> dict[str, list[ResourceId]]:
        result:dict[str, list[ResourceId]] = {}

        for name, value in key.items():
            finalValue:list[ResourceId] = []

            if isinstance(value, str) or isinstance(value, ResourceId):
                finalValue = [ ResourceId.parse(value) ]
            elif isinstance(value, Iterable):
                finalValue = [ ResourceId.parse(e) for e in value ]

            if len(name) != 1:
                raise ValueError(f"key names must be a single letter (\"{name}\" is not valid)")

            result[name] = finalValue

        return result

    def _parsePattern(self, pattern:Iterable[str]) -> list[str]:
        result:list[str] = []

        for row in pattern:
            if len(row) not in [2, 3]:
                raise ValueError(f"pattern rows must be 2 or 3 letters: (\"{row}\" is not valid)")

            result.append(row)

        return result
