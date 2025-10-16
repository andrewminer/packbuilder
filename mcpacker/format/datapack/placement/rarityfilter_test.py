from mcpacker.format.datapack.placement.rarityfilter import RarityFilter
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="placement")
def createPlacement():
    yield RarityFilter(4)


# Tests ############################################################################################

def test_asData(placement):
    assert placement.asData() == {
        "type": "minecraft:rarity_filter",
        "chance": 4
    }

