from pytest import fixture
from tungston.generator.datapack.placement.insquare import InSquare


# Fixtures #########################################################################################

@fixture(name="placement")
def createPlacement():
    yield InSquare()


# Tests ############################################################################################

def test_asData(placement):
    assert placement.asData() == {
        "type": "minecraft:in_square",
    }

