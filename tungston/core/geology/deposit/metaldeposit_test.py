from pytest import fixture
from tungston.core.ecology.biomefilter import BiomeFilter
from tungston.core.geology.deposit.metaldeposit import MetalDeposit
from tungston.core.geology.inclusion import Inclusion
from tungston.core.geology.mineral import Mineral
from tungston.core.geology.replacement import Replacement

import tungston.core.ecology.flora      as FL
import tungston.core.geology.bulk       as BU
import tungston.core.geology.proportion as PR
import tungston.core.scarcity           as SC


# Fixtures #########################################################################################

@fixture(name="quartz")
def createQuartz():
    yield Mineral("quartz", [
        Replacement("#minecraft:stone_replaceables", "minecraft:quartz_ore"),
        Replacement("#minecraft:deepslate_replaceables", "minecraft:deepslate_quartz_ore")
    ])

@fixture(name="iron")
def createIron():
    yield Mineral("iron", [
        Replacement("#minecraft:stone_replaceables", "minecraft:iron_ore"),
        Replacement("#minecraft:deepslate_replaceables", "minecraft:deepslate_iron_ore")
    ])

@fixture(name="bifIron")
def createBifIron(iron, quartz):
    yield MetalDeposit(
        name = "bifiron",
        biomeFilter = BiomeFilter([FL.FOREST]),
        bulk = BU.LARGE,
        inclusions = [Inclusion(iron, 60), Inclusion(quartz, 40)],
        proportion = PR.LENS,
        scarcity = SC.COMMON,
    )

# Tests ############################################################################################

def test_repr(bifIron):
    assert repr(bifIron) == (
        "MetalDeposit<bifiron>{" +
            "scarcity: Scarcity<common>, " +
            "biomeFilter: BiomeFilter([[Flora<forest>]], [[]]), " +
            "inclusions: [" +
                "Inclusion{mineral: iron, weight: 60}, " +
                "Inclusion{mineral: quartz, weight: 40}" +
            "], " +
            "bulk: Bulk<small>{smallest: 1000, largest: 2000}, " +
            "proportion: Proportion<lens>{ratio: 0.4}" +
        "}"
    )
