from mcpacker.model.ecology.biometrait import BiomeTrait
from pytest import fixture

import mcpacker.model.ecology.biometrait as biomeTrait


# Fixtures #########################################################################################

@fixture(name="blue")
def defineBlue():
    yield BiomeTrait("blue")

@fixture(name="green")
def defineGreen():
    yield BiomeTrait("green")

@fixture(name="yellow")
def defineYellow():
    yield BiomeTrait("yellow")

@fixture(name="orange")
def defineOrange():
    yield BiomeTrait("orange")

@fixture(name="red")
def defineRed():
    yield BiomeTrait("red")

@fixture(name="traitMap")
def createTraitMap(green, blue):
    yield {
        green: "emerald",
        blue: "sapphire"
    }

@fixture(name="traitList")
def createTraitList(green, blue, yellow, orange, red):
    yield [blue, green, yellow, orange, red]


# Tests ############################################################################################

def test_eq(green, blue):
    assert green == BiomeTrait("green")
    assert green != blue

def test_hash(green, blue, traitMap):
    assert traitMap[green] == "emerald"
    assert traitMap[blue] == "sapphire"

def test_repr(green):
    assert repr(green) == "BiomeTrait(name='green')"

def test_str(green):
    assert str(green) == "green"

def test_within(traitList, green, yellow, orange):
    assert biomeTrait.within(traitList, green, orange) == [green, yellow, orange]
