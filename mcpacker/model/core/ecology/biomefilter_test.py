from mcpacker.model.core.ecology.biome import Biome
from mcpacker.model.core.ecology.biomefilter import BiomeFilter
from pytest import fixture

import mcpacker.model.core.ecology.flora as F
import mcpacker.model.core.ecology.geology as G
import mcpacker.model.core.ecology.heat as E
import mcpacker.model.core.ecology.humidity as U
import mcpacker.model.core.ecology.soil as S
import mcpacker.model.core.ecology.water as W


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
