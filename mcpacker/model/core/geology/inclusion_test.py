from mcpacker.model.core.geology.inclusion import Inclusion
from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.geology.replacement import Replacement
from pytest import fixture


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
