from mcpacker.model.ecology.biome import Biome
from mcpacker.model.ecology.biomefilter import BiomeFilter
from mcpacker.model.resourceid import ResourceId
from pytest import fixture

import mcpacker.model.ecology.flora as F
import mcpacker.model.ecology.geology as G
import mcpacker.model.ecology.heat as E
import mcpacker.model.ecology.humidity as U
import mcpacker.model.ecology.soil as S
import mcpacker.model.ecology.water as W


# Fixtures #########################################################################################

@fixture(name="barren")
def createBarrenFilter():
    yield BiomeFilter([F.BARREN])

@fixture(name="barrenNotSandy")
def createBarrenNotSandFilter():
    yield BiomeFilter([F.BARREN], [S.SANDY])

@fixture(name="desert")
def createDesertBiome():
    yield Biome(
        "phoenix", "minecraft:desert",
        F.BARREN, G.SEDIMENTARY, E.TROPICAL, U.DRY, S.SANDY, W.INLAND
    )

@fixture(name="inDesert")
def createDesertFilter():
    yield BiomeFilter([ResourceId.parse("minecraft:desert")])

@fixture(name="notInDesert")
def createNotDesertFilter():
    yield BiomeFilter([], [ResourceId.parse("minecraft:desert")])

@fixture(name="fertile")
def createFertileFilter():
    yield BiomeFilter([(S.LOAMY, S.PEATY)])

@fixture(name="forest")
def createForestBiome():
    yield Biome(
        "portland", "minecraft:forest",
        F.FOREST, G.SEDIMENTARY, E.TEMPERATE, U.DAMP, S.LOAMY, W.INLAND
    )

@fixture(name="notDry")
def createNotDryFilter():
    yield BiomeFilter([], [U.DRY])


# Tests ############################################################################################

def test_prohibitsSingleTrait(notDry, desert, forest):
    assert notDry.accepts(forest)
    assert not notDry.accepts(desert)

def test_requireSingleTrait(barren, desert, forest):
    assert barren.accepts(desert)
    assert not barren.accepts(forest)

def test_requireOptions(fertile, desert, forest):
    assert fertile.accepts(forest)
    assert not fertile.accepts(desert)

def test_vetoed(barrenNotSandy, desert):
    assert not barrenNotSandy.accepts(desert)

def test_requiredBiome(inDesert, desert, forest):
    assert inDesert.accepts(desert)
    assert not inDesert.accepts(forest)

def test_prohibitedBiome(notInDesert, desert, forest):
    assert not notInDesert.accepts(desert)
    assert notInDesert.accepts(forest)
