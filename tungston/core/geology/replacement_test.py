from pytest import fixture
from tungston.core.geology.replacement import Replacement


# Fixtures #########################################################################################

@fixture(name="replacement")
def createReplacement():
    yield Replacement("#minecraft:stone", "minecraft:iron_ore")

@fixture(name="weightedReplacement")
def createWeightedReplacement():
    yield Replacement("#minecraft:dirt", "minecraft:gravel", 25)


# Tests ############################################################################################

def test_repr(replacement, weightedReplacement):
    assert repr(replacement) == (
        "Replacement{source: #minecraft:stone, target: minecraft:iron_ore, weight: 100}"
    )
    assert repr(weightedReplacement) == (
        "Replacement{source: #minecraft:dirt, target: minecraft:gravel, weight: 25}"
    )

def test_str(replacement, weightedReplacement):
    assert str(replacement) == "#minecraft:stone => minecraft:iron_ore"
    assert str(weightedReplacement) == "#minecraft:dirt => minecraft:gravel (25%)"
