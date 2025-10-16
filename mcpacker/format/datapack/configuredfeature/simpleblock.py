from mcpacker.json                              import JsonBlob
from mcpacker.format.datapack.blockstateprovider import BlockStateProvider
from mcpacker.format.datapack.configuredfeature  import ConfiguredFeature
from typing                                     import Any


# Class ############################################################################################

class SimpleBlock(ConfiguredFeature):

    def __init__(self, toPlace:BlockStateProvider):
        super().__init__("minecraft:simple_block")
        self.toPlace = toPlace

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": self.gameId,
            "config": {
                "to_place": self.toPlace.asJsonBlob()
            }
        }
