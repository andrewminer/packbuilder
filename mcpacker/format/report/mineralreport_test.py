from mcpacker.format.report.mineralreport import MineralReport
from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.geology.replacement import Replacement
from mcpacker.model.modpack import AugmentFunc
from mcpacker.model.modpack import ModPack
from pytest import fixture

import textwrap


# Fixtures #########################################################################################

@fixture(name="addMinerals")
def defineAddMinerals():
    def addMinerals(pack:ModPack):
        pack.world.minerals.add(Mineral("copper", [
            Replacement("#minecraft:stone_replaceables", "minecraft:copper_ore"),
            Replacement("#minecraft:deepslate_replaceables", "minecraft:deepslate_copper_ore")
        ]))

        pack.world.minerals.add(Mineral("iron", [
            Replacement("#minecraft:stone_replaceables", "minecraft:iron_ore"),
            Replacement("#minecraft:deepslate_replaceables", "minecraft:deepslate_iron_ore")
        ]))

    return addMinerals

@fixture(name="pack")
def createPack(addMinerals:AugmentFunc):
    yield ModPack("testModPack").augment(addMinerals)

@fixture(name="report")
def createReport(pack:ModPack):
    yield MineralReport(pack).compose()


# Tests ############################################################################################

def test_report(report:MineralReport):
    assert str(report).strip() == textwrap.dedent("""
        Mineral: copper

            #minecraft:stone_replaceables => minecraft:copper_ore
            #minecraft:deepslate_replaceables => minecraft:deepslate_copper_ore

        Mineral: iron

            #minecraft:stone_replaceables => minecraft:iron_ore
            #minecraft:deepslate_replaceables => minecraft:deepslate_iron_ore
    """).strip()
