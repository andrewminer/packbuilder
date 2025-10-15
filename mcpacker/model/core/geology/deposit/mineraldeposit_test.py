from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.geology.deposit.mineraldeposit import MineralDeposit
from mcpacker.model.core.geology.inclusion import Inclusion
from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.geology.replacement import Replacement
from pytest import fixture

import mcpacker.model.core.ecology.flora      as FL
import mcpacker.model.core.geology.bulk       as BU
import mcpacker.model.core.geology.proportion as PR
import mcpacker.model.core.scarcity           as SC


# Fixtures #########################################################################################

@fixture(name="quartz")
def createQuartz():
    yield Mineral("quartz", [])

@fixture(name="iron")
def createIron():
    yield Mineral("iron", [])

@fixture(name="bifIron")
def createBifIron(iron, quartz):
    yield MineralDeposit(
        name = "bifiron",
        biomeFilters = BiomeFilter([FL.FOREST]),
        bulk = BU.LARGE,
        inclusions = [Inclusion(iron, 60), Inclusion(quartz, 40)],
        proportion = PR.LENS,
        scarcity = SC.COMMON,
    )

# Tests ############################################################################################

def test_repr(bifIron):
    assert repr(bifIron) == (
        "MineralDeposit(" +
            "name='bifiron', " +
            "altitude=Altitude(name=anywhere, bottom=-64, top=320), " +
            "biomeFilters=[BiomeFilter(required=[Flora(name='forest')], prohibited=[])], " +
            "bulk=Bulk(name='large', smallest=1250, largest=1500), " +
            "inclusions=[" +
                "Inclusion(mineral=Mineral(name='iron', replacements=[]), weight=60), " +
                "Inclusion(mineral=Mineral(name='quartz', replacements=[]), weight=40)" +
            "], " +
            "proportion=Proportion(name='lens', ratio=0.4), " +
            "scarcity=Scarcity(name='common')" +
        ")"
    )
