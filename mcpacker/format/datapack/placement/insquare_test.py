from mcpacker.format.datapack.placement.insquare import InSquare
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="placement")
def createPlacement():
    yield InSquare()


# Tests ############################################################################################

def test_asData(placement):
    assert placement.asJsonBlob() == {
        "type": "minecraft:in_square",
    }

