from mcpacker.model.datapack.placement import Placement
from typing import Any

# Class ############################################################################################

class Biome(Placement):

    def __init__(self):
        super().__init__("minecraft:biome")

    def asData(self) -> dict[str,Any]:
        return { "type": self.gameId }

