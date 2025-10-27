from collections.abc import Iterable
from mcpacker.format.json import JsonBlob
from mcpacker.model.resourceid import ResourceId


# Class ############################################################################################

class RemoveSpawnBiomeModifier:

    def __init__(self, biomes:Iterable[str]|str, entityTypes:Iterable[ResourceId]):
        if isinstance(biomes, str):
            biomes = [biomes]

        self.biomes = biomes
        self.entityTypes = entityTypes

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": "neoforge:remove_spawns",
            "biomes": list(self.biomes),
            "entity_types": [str(r) for r in self.entityTypes],
        }
