from collections.abc import Iterable
from mcpacker.model.resourceid import ResourceId
from mcpacker.json import JsonBlob

import mcpacker.format.datapack.heightmaptype as HM
import mcpacker.format.datapack.generationstep as GS


# Class ############################################################################################

class Structure:

    def __init__(
        self,
        gameId:ResourceId,
        biomes:Iterable[ResourceId],
    ):
        self.gameId = gameId
        self.biomes = list(biomes)

    def asJsonBlob(self) -> JsonBlob:
        return {
            "biomes": [str(b) for b in self.biomes],
            "max_distance_from_center": 10,
            "project_start_to_heightmap": str(HM.OCEAN_FLOOR),
            "size": 1,
            "spawn_overrides": {},
            "start_height": { "absolute": 0 },
            "start_pool": f"{self.gameId.mod}:deposit/{self.gameId.name}_marker",
            "step": str(GS.SURFACE_STRUCTURES),
            "type": "minecraft:jigsaw",
            "use_expansion_hack": False,
        }
