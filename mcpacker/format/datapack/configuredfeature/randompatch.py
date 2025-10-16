from mcpacker.format.datapack.configuredfeature import ConfiguredFeature
from mcpacker.json import JsonBlob
from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mcpacker.format.datapack.placedfeature import PlacedFeature


# Class ############################################################################################

class RandomPatch(ConfiguredFeature):

    def __init__(
        self,
        gameId:str,
        feature:"PlacedFeature",
        tries:int=128,
        xzSpread:int=7,
        ySpread:int=3,
    ):
        super().__init__("minecraft:random_patch")

        self.feature = feature
        self.tries = tries
        self.xzSpread = xzSpread
        self.ySpread = ySpread

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": self.gameId,
            "feature": self.feature.gameId,
            "tries": self.tries,
            "xz_spread": self.xzSpread,
            "y_spread": self.ySpread
        }
