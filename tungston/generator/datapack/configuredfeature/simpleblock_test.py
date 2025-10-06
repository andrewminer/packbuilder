from pytest import fixture
from tungston.generator.datapack.blockstate import BlockState
from tungston.generator.datapack.blockstateprovider.simplestateprovider import SimpleStateProvider
from tungston.generator.datapack.configuredfeature.simpleblock import SimpleBlock


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
