from mcpacker.model.datapack.placement.biome import Biome
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="placement")
def createPlacement():
    yield Biome()


# Tests ############################################################################################

def test_asData(placement):
    assert placement.asData() == {
        "type": "minecraft:biome",
    }

