from pytest import fixture
from tungston.generator.datapack.placement.biome import Biome


# Fixtures #########################################################################################

@fixture(name="placement")
def createPlacement():
    yield Biome()


# Tests ############################################################################################

def test_asData(placement):
    assert placement.asData() == {
        "type": "minecraft:biome",
    }

