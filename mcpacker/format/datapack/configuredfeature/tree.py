from mcpacker.model.flora.tree import Tree
from mcpacker.format.json import JsonBlob

import mcpacker.model.flora.trunkshape as TR
import math


# Class ############################################################################################

class TreeConfiguredFeature:

    def __init__(self, tree:Tree):
        self.tree = tree

    def asJsonBlob(self) -> JsonBlob:
        return {
            "type": "minecraft:tree",
            "config": {
                "dirt_provider": self._buildDirtProvider(),
                "foliage_placer": self._buildFoliagePlacer(),
                "foliage_provider": self._buildFoliageProvider(),
                "force_dirt": False,
                "ignore_vines": True,
                "minimum_size": self._buildMinimumSize(),
                "trunk_placer": self._buildTrunkPlacer(),
                "trunk_provider": self._buildTrunkProvider(),
            }
        }


    # Private Methods ##########################################################

    def _buildDirtProvider(self) -> JsonBlob:
        return {
            "type": "minecraft:simple_state_provider",
            "state": { "Name": "minecraft:dirt" },
        }

    def _buildFoliagePlacer(self) -> JsonBlob:
        return {
            "type": f"minecraft:{self.tree.canopyShape!s}_foliage_placer",
            "height": max(1, self.tree.canopyHeight),
            "offset": 0,
            "radius": self.tree.canopyRadius,
        }

    def _buildFoliageProvider(self) -> JsonBlob:
        properties:dict[str, JsonBlob] = {
            "distance": str(math.ceil(self.tree.canopyRadius * 1.5)),
            "persistent": "false",
            "waterlogged": "false",
        }
        if self.tree.foliage.mod == "fruitsdelight":
            properties["type"] = "leaves"

        return {
            "type": "minecraft:simple_state_provider",
            "state": {
                "Name": str(self.tree.foliage),
                "Properties": properties,
            }
        }

    def _buildMinimumSize(self) -> JsonBlob:
        return {
            "type": "minecraft:two_layers_feature_size",
            "limit": 1,
            "lower_size": 0,
            "upper_size": 1,
        }

    def _buildTrunkPlacer(self) -> JsonBlob:
        return {
            "type": f"minecraft:{self.tree.trunkShape!s}_trunk_placer",
            "base_height": self.tree.trunkHeightMin,
            "height_rand_a": self.tree.trunkHeightMax - self.tree.trunkHeightMin,
            "height_rand_b": 0,
        }

    def _buildTrunkProvider(self) -> JsonBlob:
        return {
            "type": "minecraft:simple_state_provider",
            "state": {
                "Name": str(self.tree.log),
                "Properties": { "axis": "y" },
            },
        }
