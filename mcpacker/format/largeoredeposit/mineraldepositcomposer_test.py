from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from mcpacker.model.core.geology.deposit.mineraldeposit import MineralDeposit
from mcpacker.model.core.geology.inclusion import Inclusion
from mcpacker.model.core.geology.mineral import Mineral
from mcpacker.model.core.geology.replacement import Replacement
from pytest import fixture
from mcpacker.format.largeoredeposit.mineraldepositcomposer import MineralDepositComposer
from pytest import fixture

import mcpacker.model.core.altitude as AL
import mcpacker.model.core.ecology.flora as FL
import mcpacker.model.core.geology.bulk as BU
import mcpacker.model.core.geology.proportion as PR
import mcpacker.model.core.scarcity as SC
import textwrap


# Fixtures #########################################################################################

@fixture(name="quartz")
def createQuartz():
    yield Mineral("quartz", [
        Replacement.inStone("quartz_ore"),
        Replacement.inDeepslate("deepslate_quartz_ore"),
    ])

@fixture(name="iron")
def createIron():
    yield Mineral("iron", [
        Replacement.inStone("iron_ore"),
        Replacement.inDeepslate("deepslate_iron_ore"),
    ])

@fixture(name="bifIron")
def createBifIron(iron, quartz):
    yield MineralDeposit(
        name = "bifiron",
        altitude = AL.CRUST,
        biomeFilters = BiomeFilter([FL.FOREST]),
        bulk = BU.LARGE,
        inclusions = [Inclusion(iron, 60), Inclusion(quartz, 40)],
        proportion = PR.LENS,
        scarcity = SC.COMMON,
    )

@fixture(name="composer")
def createComposer(bifIron):
    yield MineralDepositComposer(bifIron).compose()

# Tests ############################################################################################

def test_str(composer):
    assert str(composer) == textwrap.dedent("""
        Config {
            B:enabled = true
        }

        Deposit {
            S:customReplacements <
                #minecraft:deepslate_ore_replaceables->minecraft:deepslate_iron_ore,60
                #minecraft:deepslate_ore_replaceables->minecraft:deepslate_quartz_ore,40
            >
            S:ores <
                minecraft:iron_ore,60
                minecraft:quartz_ore,40
            >
            I:rarity=9
            S:replaceableBlocks <
                #minecraft:stone_ore_replaceables
            >
            B:vanilla=false
            Dimensions {
                S:blackList <
                >
                S:whiteList <
                >
            }
            Biomes {
                S:blackList <
                >
                S:whiteList <
                >
            }
            Altitude {
                I:min=-32
                I:max=32
            }
            Miscellaneous {
                B:exposed=true
                S:proportions=0.40
                B:strictBounds=false
                B:strictStart=false
            }
            Indicator {
                S:circles <
                >
                S:continuity=0
                I:distortion=0
                S:id=deposit/bifiron_marker
                S:threshold=100
            }
            Size {
                i:min=1250
                I:max=1500
            }
        }
    """).strip()
