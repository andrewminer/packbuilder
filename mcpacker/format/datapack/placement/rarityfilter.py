from mcpacker.format.datapack.placement import Placement
from mcpacker.json import JsonBlob
from typing import Any


# Class ############################################################################################

class RarityFilter(Placement):

    def __init__(self, chance:int):
        super().__init__("minecraft:rarity_filter")
        self.chance = chance

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": self.gameId,
            "chance": self.chance,
        }

