from mcpacker.model.datapack.blockstate import BlockState
from mcpacker.model.datapack.blockstateprovider.simplestateprovider import SimpleStateProvider
from mcpacker.model.datapack.configuredfeature.simpleblock import SimpleBlock
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="state")
def createBlockState():
    yield BlockState("minecraft:button", {"waterlogged": "true"})

@fixture(name="provider")
def createProvider(state):
    return SimpleStateProvider(state)

@fixture(name="feature")
def createSimpleBlockFeature(provider):
    return SimpleBlock(provider)


# Tests ############################################################################################

def test_asData(feature):
    assert feature.asData() == {
        "type": "minecraft:simple_block",
        "config": {
            "to_place": {
                "type": "minecraft:simple_state_provider",
                "state": {
                    "Name": "minecraft:button",
                    "Properties": {
                        "waterlogged": "true"
                    }
                }
            }
        }
    }
