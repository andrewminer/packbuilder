from collections.abc import Iterable
from mcpacker.format.datapack.placement import Placement
from mcpacker.json import JsonBlob


# Class ############################################################################################

class PlacedFeature:

    def __init__(self, gameId:str, placements:Iterable[Placement]):
        self.gameId = gameId
        self.placements = placements

    def asJsonBlob(self) -> JsonBlob:
        return {
            "feature": self.gameId,
            "placements": [p.asJsonBlob() for p in self.placements],
        }
