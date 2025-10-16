from mcpacker.format.datapack.blockstate import BlockState
from mcpacker.format.datapack.blockstateprovider.simplestateprovider import SimpleStateProvider
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="state")
def createBlockState():
    yield BlockState("minecraft:button", {"waterlogged": "true"})

@fixture(name="provider")
def createProvider(state:BlockState):
    return SimpleStateProvider(state)


# Tests ############################################################################################

def test_asData(provider:SimpleStateProvider):
    assert provider.asJsonBlob() == {
        "type": "minecraft:simple_state_provider",
        "state": {
            "Name": "minecraft:button",
            "Properties": {
                "waterlogged": "true"
            }
        }
    }
