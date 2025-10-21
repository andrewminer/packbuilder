from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.geology.replacement import Replacement
from pytest import fixture

import mcpacker.model.geology.mineral as mineral


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
        "Mineral(" +
            "name='iron', " +
            "replacements=[" +
                "Replacement(" +
                    "source='#minecraft:stone_ore_replaceables', " +
                    "target='minecraft:iron_ore', " +
                    "weight=100" +
                "), " +
                "Replacement(" +
                    "source='#minecraft:deepslate_ore_replaceables', " +
                    "target='minecraft:deepslate_iron_ore', " +
                    "weight=100" +
                ")"
            "]" +
        ")"
    )
