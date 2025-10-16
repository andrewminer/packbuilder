from mcpacker.format.datapack.blockstate import BlockState
from mcpacker.format.datapack.placedfeature import PlacedFeature
from mcpacker.format.datapack.blockstateprovider.simplestateprovider import SimpleStateProvider
from mcpacker.format.datapack.configuredfeature.randompatch import RandomPatch
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="state")
def createBlockState():
    yield BlockState("minecraft:button", {"waterlogged": "true"})

@fixture(name="provider")
def createProvider(state:BlockState):
    return SimpleStateProvider(state)

@fixture(name="placedFeature")
def createPlacedFeature():
    return PlacedFeature("noop", [])

@fixture(name="feature")
def createFeature(placedFeature:PlacedFeature):
    return RandomPatch("test", placedFeature)


# Tests ############################################################################################

def test_asJsonBlob(feature:RandomPatch):
    assert feature.asJsonBlob() == {
        "type": "minecraft:random_patch",
        "feature": "noop",
        "tries": 128,
        "xz_spread": 7,
        "y_spread": 3,
    }
