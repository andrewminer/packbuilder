from mcpacker.format.datapack.blockstate import BlockState
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="state")
def createBlockState():
    yield BlockState("minecraft:button", {"waterlogged": "true"})


# Tests ############################################################################################

def test_asData(state:BlockState):
    assert state.asJsonBlob() == {
        "Name": "minecraft:button",
        "Properties": {
            "waterlogged": "true"
        }
    }
