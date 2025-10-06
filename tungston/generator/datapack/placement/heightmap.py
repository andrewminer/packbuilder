from tungston.generator.datapack.placement import Placement
from tungston.generator.datapack.heightmaptype import HeightMapType
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
