from mcpacker.format.datapack.placedfeature.crop import CropPlacedFeature
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

@fixture(name="farmCropBlob")
def createFarmCropBlob(pack:ModPack):
    yield CropPlacedFeature(
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

@fixture(name="waterAdjacentCropBlob")
def createWaterAdjacentBlob(pack:ModPack):
    yield CropPlacedFeature(
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

@fixture(name="submergedCropBlob")
def createSubmergedCropBlob(pack:ModPack):
    yield CropPlacedFeature(
        pack = pack,
        spawn = PlantSpawn(
            name = "rice",
            habitat = Habitat(
                altitude = AL.SURFACE,
                biomeFilters = BF([(WA.RIVER, WA.SWAMP)]),
            ),
            ecotype = Ecotype(
                scarcity = SC.UNCOMMON,
            ),
            plant = Patch(
                name = "rice",
                blocks = "farmersdelight:wild_rice",
                density = DE.PACKED,
                immersion = IM.SUBMERGED,
                radius = 6,
                substrates = [ "minecraft:sand", "minecraft:dirt" ],
            ),
        ),
    ).asJsonBlob()


# Tests ############################################################################################

def test_farmCrop(farmCropBlob:JsonBlob):
    assert dumps(farmCropBlob) == textwrap.dedent("""
        {
            "feature": "test:crop/potato",
            "placement": [
                {
                    "type": "minecraft:block_predicate_filter",
                    "predicate": [
                        {
                            "type": "minecraft:matching_blocks",
                            "blocks": "minecraft:air"
                        },
                        {
                            "type": "minecraft:matching_blocks",
                            "offset": [
                                0,
                                -1,
                                0
                            ],
                            "blocks": [
                                "#minecraft:dirt"
                            ]
                        }
                    ]
                }
            ]
        }
    """).strip()

def test_submergedCrop(submergedCropBlob:JsonBlob):
    assert dumps(submergedCropBlob) == textwrap.dedent("""
        {
            "feature": "test:crop/rice",
            "placement": [
                {
                    "type": "minecraft:block_predicate_filter",
                    "predicate": [
                        {
                            "type": "minecraft:matching_blocks",
                            "blocks": "minecraft:water"
                        },
                        {
                            "type": "minecraft:matching_blocks",
                            "offset": [
                                0,
                                -1,
                                0
                            ],
                            "blocks": [
                                "minecraft:sand",
                                "minecraft:dirt"
                            ]
                        }
                    ]
                }
            ]
        }
    """).strip()

def test_waterAdjacentCrop(waterAdjacentCropBlob:JsonBlob):
    assert dumps(waterAdjacentCropBlob) == textwrap.dedent("""
        {
            "feature": "test:crop/sugarcane",
            "placement": [
                {
                    "type": "minecraft:block_predicate_filter",
                    "predicate": [
                        {
                            "type": "minecraft:matching_blocks",
                            "blocks": "minecraft:air"
                        },
                        {
                            "type": "minecraft:matching_blocks",
                            "offset": [
                                0,
                                -1,
                                0
                            ],
                            "blocks": [
                                "#minecraft:dirt"
                            ]
                        }
                    ]
                },
                {
                    "type": "minecraft:any_of",
                    "predicates": [
                        {
                            "type": "minecraft:matching_fluids",
                            "fluids": [
                                "minecraft:water",
                                "minecraft:flowing_water"
                            ],
                            "offset": [
                                1,
                                -1,
                                0
                            ]
                        },
                        {
                            "type": "minecraft:matching_fluids",
                            "fluids": [
                                "minecraft:water",
                                "minecraft:flowing_water"
                            ],
                            "offset": [
                                -1,
                                -1,
                                0
                            ]
                        },
                        {
                            "type": "minecraft:matching_fluids",
                            "fluids": [
                                "minecraft:water",
                                "minecraft:flowing_water"
                            ],
                            "offset": [
                                0,
                                -1,
                                1
                            ]
                        },
                        {
                            "type": "minecraft:matching_fluids",
                            "fluids": [
                                "minecraft:water",
                                "minecraft:flowing_water"
                            ],
                            "offset": [
                                0,
                                -1,
                                -1
                            ]
                        }
                    ]
                }
            ]
        }
    """).strip()

