from mcpacker.model.datapack.heightmaptype import HeightMapType
from mcpacker.model.datapack.placement import Placement
from typing import Any

# Class ############################################################################################

class HeightMap(Placement):

    def __init__(self, heightMap:HeightMapType):
        super().__init__("minecraft:heightmap")
        self.heightMap = heightMap

    def asData(self) -> dict[str,Any]:
        return {
            "type": self.gameId,
            "heightmap": self.heightMap.asData()
        }
