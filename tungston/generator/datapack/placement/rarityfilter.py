from tungston.generator.datapack.placement import Placement
from typing import Any

# Class ############################################################################################

class RarityFilter(Placement):

    def __init__(self, chance:int):
        super().__init__("minecraft:rarity_filter")
        self.chance = chance

    def asData(self) -> dict[str,Any]:
        return {
            "type": self.gameId,
            "chance": self.chance
        }

