from mcpacker.format.datapack.placedfeature.patch import PatchPlacedFeature
from mcpacker.format.json import JsonBlob
from mcpacker.model.ecology.biomefilter import BiomeFilter as BF
from mcpacker.model.ecotype import Ecotype
from mcpacker.model.flora.patch import Patch
from mcpacker.model.flora.plantspawn import PlantSpawn
from mcpacker.model.flora.tree import Tree
from mcpacker.model.habitat import Habitat
from mcpacker.model.modpack import ModPack
from mcpacker.write.json import dumps
from pytest import fixture

import mcpacker.model.altitude as AL
import mcpacker.model.ecology.flora as FL
import mcpacker.model.ecology.heat as HE
import mcpacker.model.ecology.humidity as HU
import mcpacker.model.ecology.soil as SO
import mcpacker.model.ecology.water as WA
import mcpacker.model.flora.canopyshape as CA
import mcpacker.model.flora.density as DE
import mcpacker.model.flora.immersion as IM
import mcpacker.model.flora.trunkshape as TR
import mcpacker.model.scarcity as SC
import textwrap


# Fixtures #########################################################################################

@fixture(name="pack")
def createModPack():
    yield ModPack("test")

@fixture(name="farmPatchBlob")
def createFarmPatchBlob(pack:ModPack):
    yield PatchPlacedFeature(
        altitude = AL.UPLANDS,
        pack = pack,
        spawn = PlantSpawn(
            name = "potato",
            habitat = Habitat(
                altitude = AL.span(AL.UPLANDS, AL.HILLS),
                biomeFilters = BF([FL.FOREST, HE.BOREAL, HU.DAMP, SO.ACIDIC]),
            ),
            ecotype = Ecotype(
                scarcity = SC.UNCOMMON,
            ),
            plant = Patch(
                name = "potato",
                blocks = "farmersdelight:wild_potatoes",
                density = DE.THIN,
                radius = 4,
            ),
        ),
    ).asJsonBlob()

@fixture(name="waterAdjacentBlob")
def createWaterAdjacentBlob(pack:ModPack):
    yield PatchPlacedFeature(
        altitude = AL.DUNES,
        pack = pack,
        spawn = PlantSpawn(
            name = "sugarcane",
            habitat = Habitat(
                altitude = AL.DUNES,
                biomeFilters = BF([(WA.RIVER, WA.SWAMP)]),
            ),
            ecotype = Ecotype(
                scarcity = SC.COMMON,
            ),
            plant = Patch(
                name = "sugarcane",
                blocks = "minecraft:sugarcane",
                density = DE.CARPET,
                immersion = IM.ADJACENT,
                radius = 3,
            ),
        ),
    ).asJsonBlob()

@fixture(name="treeBlob")
def createTreeBlob(pack:ModPack):
    yield PatchPlacedFeature(
        altitude = AL.LOWLANDS,
        pack = pack,
        spawn = PlantSpawn(
            name = "apple",
            habitat = Habitat(
                altitude = AL.LOWLANDS,
                biomeFilters = BF([(FL.FOREST, FL.CLEARING), HE.TEMPERATE, SO.LOAMY]),
            ),
            ecotype = Ecotype(
                scarcity = SC.SPARSE,
            ),
            plant = Tree(
                name = "apple",
                foliage = "fruitsdelight:apple_leaves",
                log = "minecraft:oak_log",
                trunkShape = TR.STRAIGHT,
                trunkHeightMin = 3,
                trunkHeightMax = 5,
                canopyShape = CA.BLOB,
                canopyHeight = 3,
                canopyRadius = 2
            )
        )
    ).asJsonBlob()


# Tests ############################################################################################

def test_farmPatch(farmPatchBlob:JsonBlob):
    assert dumps(farmPatchBlob) == textwrap.dedent("""
        {
            "feature": "test:patch/potato",
            "placement": [
                {
                    "type": "mincraft:rarity_filter",
                    "chance": 8
                },
                {
                    "type": "minecraft:in_square"
                },
                {
                    "type": "minecraft:biome"
                },
                {
                    "type": "minecraft:height_range",
                    "height": {
                        "type": "minecraft:constant",
                        "value": {
                            "absolute": 92
                        }
                    }
                },
                {
                    "type": "minecraft:block_predicate_filter",
                    "predicate": {
                        "type": "minecraft:matching_blocks",
                        "blocks": "minecraft:air"
                    }
                },
                {
                    "type": "minecraft:environment_scan",
                    "direction_of_search": "up",
                    "max_steps": 32,
                    "target_condition": {
                        "type": "minecraft:matching_blocks",
                        "blocks": "minecraft:air"
                    }
                }
            ]
        }
    """).strip()

def test_tree(treeBlob:JsonBlob):
    assert dumps(treeBlob) == textwrap.dedent("""
        {
            "feature": "test:tree/apple",
            "placement": [
                {
                    "type": "mincraft:rarity_filter",
                    "chance": 16
                },
                {
                    "type": "minecraft:in_square"
                },
                {
                    "type": "minecraft:biome"
                },
                {
                    "type": "minecraft:height_range",
                    "height": {
                        "type": "minecraft:constant",
                        "value": {
                            "absolute": 70
                        }
                    }
                },
                {
                    "type": "minecraft:block_predicate_filter",
                    "predicate": {
                        "type": "minecraft:matching_blocks",
                        "blocks": "minecraft:air"
                    }
                },
                {
                    "type": "minecraft:environment_scan",
                    "direction_of_search": "up",
                    "max_steps": 22,
                    "target_condition": {
                        "type": "minecraft:matching_blocks",
                        "blocks": "minecraft:air"
                    }
                }
            ]
        }
    """).strip()
