from mcpacker.format.datapack.heightmaptype import WORLD_SURFACE
from mcpacker.format.datapack.placement.heightmap import HeightMap
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="placement")
def createPlacement():
    yield HeightMap(WORLD_SURFACE)


# Tests ############################################################################################

def test_asData(placement):
    assert placement.asData() == {
        "type": "minecraft:heightmap",
        "heightmap": "WORLD_SURFACE"
    }

