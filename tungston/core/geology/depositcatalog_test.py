from pytest import fixture
from tungston.core.ecology.biomefilter import BiomeFilter
from tungston.core.geology.deposit import Deposit
from tungston.core.geology.deposit.metaldeposit import MetalDeposit
from tungston.core.geology.depositcatalog import DepositCatalog
from tungston.core.geology.inclusion import Inclusion
from tungston.core.geology.mineral import Mineral
from tungston.core.geology.replacement import Replacement

import tungston.core.ecology.flora as FL
import tungston.core.geology.bulk  as BU
import tungston.core.scarcity      as SC


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

@fixture(name="bifiron")
def createBifIron(iron, quartz):
    yield MetalDeposit(
        name = "bif_iron",
        scarcity = SC.COMMON,
        biomeFilter = BiomeFilter([FL.FOREST]),
        inclusions = [Inclusion(iron, 60), Inclusion(quartz, 40)],
        bulk = BU.LARGE,
        proportion = 0.5,
    )

@fixture(name="catalog")
def createCatalog(bifiron):
    yield DepositCatalog([bifiron])


# Tests ############################################################################################

def test_all(catalog):
    assert [m.name for m in catalog.all()] == ["bif_iron"]

def test_get(catalog):
    assert catalog.get("bif_iron").name == "bif_iron"
