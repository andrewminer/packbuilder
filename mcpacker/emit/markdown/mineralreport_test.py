from mcpacker.emit.markdown.mineralreport import MineralReport
from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.geology.mineralcatalog import MineralCatalog
from mcpacker.model.core.geology.replacement import Replacement
from mcpacker.model.core.world import World
from pytest import fixture

import textwrap


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

@fixture(name="minerals")
def createMineralCatalog(copper, iron):
    yield MineralCatalog([copper, iron])

@fixture(name="world")
def createWorld(minerals):
    yield World(None, None, minerals, None)

@fixture(name="report")
def createReport(world):
    report = MineralReport(world)
    report.build()
    yield report


# Tests ############################################################################################

def test_report(report):
    assert str(report) == textwrap.dedent("""
        # Mineral: copper

          * #minecraft:stone_replaceables => minecraft:copper_ore
          * #minecraft:deepslate_replaceables => minecraft:deepslate_copper_ore

        # Mineral: iron

          * #minecraft:stone_replaceables => minecraft:iron_ore
          * #minecraft:deepslate_replaceables => minecraft:deepslate_iron_ore
    """).strip()
