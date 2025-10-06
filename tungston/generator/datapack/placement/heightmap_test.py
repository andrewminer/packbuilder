from pytest import fixture
from tungston.generator.datapack.placement.heightmap import HeightMap
from tungston.generator.datapack.heightmaptype import WORLD_SURFACE


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

