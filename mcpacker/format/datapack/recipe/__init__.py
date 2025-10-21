from collections.abc import Iterable
from collections.abc import Mapping
from mcpacker.model.resourceid import ResourceId


# Class ############################################################################################

class Recipe:

    def __init__(
        self,
        gameId:str|ResourceId,
        resultId:str|ResourceId,
        resultCount:int=1,
        resultComponents:Mapping[str,str]|None=None,
    ):
        self.gameId           = ResourceId.parse(gameId)
        self.resultComponents = resultComponents
        self.resultCount      = resultCount
        self.resultId         = ResourceId.parse(resultId)
