from pytest import fixture
from tungston.core.geology.inclusion import Inclusion
from tungston.core.geology.mineral import Mineral
from tungston.core.geology.replacement import Replacement


# Fixtures #########################################################################################I

@fixture(name="iron")
def createIron():
    yield Mineral("iron", [
        Replacement("#minecraft:stone_replaceables", "minecraft:iron_ore"),
        Replacement("#minecraft:deepslate_replaceables", "minecraft:deepslate_iron_ore")
    ])

@fixture(name="inclusion")
def createInclusion(iron):
    yield Inclusion(iron, 75)


# Tests ############################################################################################I

def test_repr(inclusion):
    assert repr(inclusion) == "Inclusion{mineral: iron, weight: 75}"
