from mcpacker.format.datapack.configuredfeature.patch import PatchConfiguredFeature
from mcpacker.format.json import JsonBlob
from mcpacker.model.flora.companion import Companion
from mcpacker.model.flora.patch import Patch
from mcpacker.model.modpack import ModPack
from pytest import fixture

import mcpacker.model.flora.density as DE
import mcpacker.model.flora.immersion as IM
import mcpacker.write.json as json
import textwrap


# Fixtures #########################################################################################

@fixture(name="blob")
def createBlob():
    yield PatchConfiguredFeature(ModPack("test"), Patch(
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
            "type": "minecraft:random_patch",
            "config": {
                "tries": 58,
                "xz_spread": 3,
                "y_spread": 1.5,
                "feature": "test:plant/poppy"
            }
        }
    """).strip()
