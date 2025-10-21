from mcpacker.model.geology.inclusion import Inclusion
from mcpacker.model.geology.mineral import Mineral
from mcpacker.model.geology.replacement import Replacement
from pytest import fixture


# Fixtures #########################################################################################I

@fixture(name="iron")
def createIron():
    yield Mineral("iron", [])

@fixture(name="inclusion")
def createInclusion(iron):
    yield Inclusion(iron, 75)


# Tests ############################################################################################I

def test_repr(inclusion):
    assert repr(inclusion) == "Inclusion(mineral=Mineral(name='iron', replacements=[]), weight=75)"
