from tungston.core.geology.mineral import Mineral
from tungston.core.geology.replacement import Replacement
from pytest import fixture

import tungston.core.geology.mineral as mineral


# Fixtures #########################################################################################

@fixture(name="iron")
def createIron():
    yield Mineral("iron", [
        Replacement.inStone("iron_ore"),
        Replacement.inDeepslate("deepslate_iron_ore"),
    ])


# Tests ############################################################################################

def test_repr(iron):
    assert repr(iron) == (
        "Mineral<iron>{" +
            "replacements: [" +
                "#minecraft:stone_ore_replaceables => minecraft:iron_ore, " +
                "#minecraft:deepslate_ore_replaceables => minecraft:deepslate_iron_ore" +
            "]" +
        "}"
    )
