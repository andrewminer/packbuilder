from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.geology.mineralcatalog import MineralCatalog
from mcpacker.model.core.geology.replacement import Replacement
from pytest import fixture


# Fixtures #########################################################################################

@fixture(name="copper")
def createCopper():
    yield Mineral("copper", [
        Replacement("#minecraft:stone_replaceables", "minecraft:copper_ore"),
        Replacement("#minecraft:deepslate_replaceables", "minecraft:deepslate_copper_ore")
    ])

@fixture(name="iron")
def createIron():
    yield Mineral("iron", [
        Replacement("#minecraft:stone_replaceables", "minecraft:iron_ore"),
        Replacement("#minecraft:deepslate_replaceables", "minecraft:deepslate_iron_ore")
    ])

@fixture(name="catalog")
def createCatalog(copper, iron):
    yield MineralCatalog([copper, iron])


# Tests ############################################################################################

def test_all(catalog):
    assert [m.name for m in catalog.all()] == ["copper", "iron"]

def test_get(catalog):
    assert catalog.get("iron").name == "iron"
