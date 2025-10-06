from tungston.generator.datapack.configuredfeature.configuredfeature import ConfiguredFeature
from typing import Any


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

    def asData(self) -> dict[str,Any]:
        return {
            "type": self.type,
            "feature": self.feature.gameId,
            "tries": self.tries,
            "xz_spread": self.xySpread,
            "y_spread": self.ySpread
        }
