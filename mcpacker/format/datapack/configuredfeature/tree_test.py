from mcpacker.format.datapack.configuredfeature.tree import TreeConfiguredFeature
from mcpacker.format.json import JsonBlob
from mcpacker.model.flora.tree import Tree
from mcpacker.model.modpack import ModPack
from pytest import fixture

import mcpacker.model.flora.canopyshape as CA
import mcpacker.model.flora.trunkshape as TR
import mcpacker.write.json as json
import textwrap


# Fixtures #########################################################################################

@fixture(name="blob")
def createBlob():
    yield TreeConfiguredFeature(Tree(
        name = "apple",
        foliage = "fruitsdelight:apple_leaves",
        log = f"minecraft:oak_log",
        trunkShape = TR.STRAIGHT,
        trunkHeightMin = 3,
        trunkHeightMax = 5,
        canopyShape = CA.BLOB,
        canopyHeight = 3,
        canopyRadius = 2
    )).asJsonBlob()


# Tests ############################################################################################

def test_asJsonBlob(blob:JsonBlob):
    assert json.dumps(blob) == textwrap.dedent("""
        {
            "type": "minecraft:tree",
            "config": {
                "dirt_provider": {
                    "type": "minecraft:simple_state_provider",
                    "state": {
                        "Name": "minecraft:dirt"
                    }
                },
                "foliage_placer": {
                    "type": "minecraft:blob_foliage_placer",
                    "height": 3,
                    "offset": 0,
                    "radius": 2
                },
                "foliage_provider": {
                    "type": "minecraft:simple_state_provider",
                    "state": {
                        "Name": "fruitsdelight:apple_leaves",
                        "Properties": {
                            "distance": "3",
                            "persistent": "false",
                            "waterlogged": "false",
                            "type": "leaves"
                        }
                    }
                },
                "force_dirt": false,
                "ignore_vines": true,
                "minimum_size": {
                    "type": "minecraft:two_layers_feature_size",
                    "limit": 1,
                    "lower_size": 0,
                    "upper_size": 1
                },
                "trunk_placer": {
                    "type": "minecraft:straight_trunk_placer",
                    "base_height": 3,
                    "height_rand_a": 2,
                    "height_rand_b": 0
                },
                "trunk_provider": {
                    "type": "minecraft:simple_state_provider",
                    "state": {
                        "Name": "minecraft:oak_log",
                        "Properties": {
                            "axis": "y"
                        }
                    }
                }
            }
        }
    """).strip()
