from mcpacker.format.datapack.configuredfeature.crop import CropConfiguredFeature
from mcpacker.format.json import JsonBlob
from mcpacker.model.flora.companion import Companion
from mcpacker.model.flora.patch import Patch
from pytest import fixture

import mcpacker.model.flora.density as DE
import mcpacker.model.flora.immersion as IM
import mcpacker.write.json as json
import textwrap


# Fixtures #########################################################################################

@fixture(name="blob")
def createBlob():
    yield CropConfiguredFeature(Patch(
        blocks = "minecraft:poppy",
        companions = [Companion("dandelion", 25)],
        density = DE.THIN,
        immersion = IM.SUBMERGED,
        name = "poppy",
        radius = 3,
    )).asJsonBlob()


# Tests ############################################################################################

def test_asJsonBlob(blob:JsonBlob):
    assert json.dumps(blob) == textwrap.dedent("""
        {
            "type": "minecraft:simple_block",
            "config": {
                "to_place": {
                    "type": "minecraft:weighted_state_provider",
                    "entries": [
                        {
                            "data": {
                                "Name": "minecraft:poppy",
                                "Properties": {
                                    "waterlogged": "true"
                                }
                            },
                            "weight": 75
                        },
                        {
                            "data": {
                                "Name": "minecraft:dandelion"
                            },
                            "weight": 25
                        }
                    ]
                }
            }
        }
    """).strip()
