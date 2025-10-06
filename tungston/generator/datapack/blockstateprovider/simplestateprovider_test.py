from tungston.generator.datapack.blockstate import BlockState
from tungston.generator.datapack.blockstateprovider.simplestateprovider import SimpleStateProvider
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="state")
def createBlockState():
    yield BlockState("minecraft:button", {"waterlogged": "true"})

@fixture(name="provider")
def createProvider(state):
    return SimpleStateProvider(state)


# Tests ############################################################################################

def test_asData(provider):
    assert provider.asData() == {
        "type": "minecraft:simple_state_provider",
        "state": {
            "Name": "minecraft:button",
            "Properties": {
                "waterlogged": "true"
            }
        }
    }
