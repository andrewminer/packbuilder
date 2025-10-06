from tungston.generator.datapack.blockstateprovider import BlockStateProvider
from tungston.generator.datapack.configuredfeature import ConfiguredFeature
from typing import Any


# Class ############################################################################################

class SimpleBlock(ConfiguredFeature):

    def __init__(self, toPlace:BlockStateProvider):
        super().__init__("minecraft:simple_block")
        self.toPlace = toPlace

    def asData(self) -> dict[str, Any]:
        return {
            "type": self.gameId,
            "config": {
                "to_place": self.toPlace.asData()
            }
        }
