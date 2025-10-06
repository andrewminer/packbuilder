from pytest import fixture
from tungston.generator.datapack.blockstate import BlockState


# Fixtures #########################################################################################

@fixture(name="state")
def createBlockState():
    yield BlockState("minecraft:button", {"waterlogged": "true"})


# Tests ############################################################################################

def test_asData(state):
    assert state.asData() == {
        "Name": "minecraft:button",
        "Properties": {
            "waterlogged": "true"
        }
    }
