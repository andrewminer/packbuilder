from mcpacker.format.resourcepack.variant import Variant
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="variant")
def createVariant():
    yield Variant("grass", 90, 180, True, 10)


# Tests ############################################################################################

def test_variant(variant:Variant):
    assert str(variant.model) == "minecraft:grass"
    assert variant.x == 90
    assert variant.uvlock == True
