from mcpacker.format.datapack.blockstate import BlockState
from mcpacker.format.datapack.blockstateprovider.simplestateprovider import SimpleStateProvider
from mcpacker.format.datapack.configuredfeature.simpleblock import SimpleBlock
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="state")
def createBlockState():
    yield BlockState("minecraft:button", {"waterlogged": "true"})

@fixture(name="provider")
def createProvider(state:BlockState):
    return SimpleStateProvider(state)

@fixture(name="feature")
def createSimpleBlockFeature(provider:SimpleStateProvider):
    return SimpleBlock(provider)


# Tests ############################################################################################

def test_asData(feature:SimpleBlock):
    assert feature.asJsonBlob() == {
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
